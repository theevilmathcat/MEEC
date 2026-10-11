import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# Set random seed for reproducibility
np.random.seed(42)

# ============================================================
# 1. Generate a known true bimodal distribution
# ============================================================
true_dist = lambda x: (0.4 * np.exp(-0.5 * ((x + 2) / 0.8) ** 2) +
                       0.6 * np.exp(-0.5 * ((x - 2) / 1.0) ** 2))

x_grid = np.linspace(-6, 6, 1000)
true_density = true_dist(x_grid)
true_density /= np.trapz(true_density, x_grid)

# ============================================================
# 2. Draw samples of increasing size
# ============================================================
n_samples_list = [20, 100, 500, 5000]

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.ravel()

# Three bandwidths to compare: too small, good, too large
bandwidths = [0.05, 0.3, 1.5]
colors = ['crimson', 'darkgreen', 'steelblue']
labels = ['h = 0.05 (demasiado pequeno)',
          'h = 0.30 (adequado)',
          'h = 1.50 (demasiado grande)']

for ax, n in zip(axes, n_samples_list):
    data = np.concatenate([
        np.random.normal(-2, 0.8, int(0.4 * n)),
        np.random.normal(2, 1.0, int(0.6 * n))
    ])

    # True density
    ax.plot(x_grid, true_density, 'k--', lw=2, label='Densidade real')
    ax.hist(data, bins=30, density=True, alpha=0.2, color='gray',
            label=f'Amostra (n={n})')

    for h, c, lab in zip(bandwidths, colors, labels):
        kde = gaussian_kde(data, bw_method=h / np.std(data))
        ax.plot(x_grid, kde(x_grid), color=c, lw=2, label=lab)

    ax.set_title(f'n = {n} amostras', fontsize=12)
    ax.set_xlim(-6, 6)
    ax.set_ylim(0, 0.5)
    ax.legend(fontsize=8, loc='upper right')
    ax.grid(alpha=0.3)

fig.suptitle('KDE: efeito da largura de banda (bandwidth) na estimativa da densidade',
             fontsize=14, y=1.00)
plt.tight_layout()
plt.savefig('kde_bandwidth.png', dpi=150, bbox_inches='tight')
plt.show()


# ============================================================
# 3. Quantify the accumulated error (ISE) vs n for each h
# ============================================================
def ise(kde_vals, true_vals, x):
    """Integrated Squared Error via trapezoidal rule."""
    return np.trapz((kde_vals - true_vals) ** 2, x)


n_reps = 30
n_values = [20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

fig2, ax2 = plt.subplots(figsize=(9, 6))

for h, c, lab in zip(bandwidths, colors, labels):
    mean_ise = []
    std_ise = []
    for n in n_values:
        errors = []
        for _ in range(n_reps):
            data = np.concatenate([
                np.random.normal(-2, 0.8, int(0.4 * n)),
                np.random.normal(2, 1.0, int(0.6 * n))
            ])
            kde = gaussian_kde(data, bw_method=h / np.std(data))
            errors.append(ise(kde(x_grid), true_density, x_grid))
        mean_ise.append(np.mean(errors))
        std_ise.append(np.std(errors))

    mean_ise = np.array(mean_ise)
    std_ise = np.array(std_ise)
    ax2.loglog(n_values, mean_ise, 'o-', color=c, lw=2, label=lab)
    ax2.fill_between(n_values, mean_ise - std_ise, mean_ise + std_ise,
                     color=c, alpha=0.2)

# Reference slopes
n_ref = np.array(n_values, dtype=float)
ax2.loglog(n_ref, 0.5 / n_ref, 'k:', lw=1, label=r'$\propto 1/n$')

ax2.set_xlabel('Tamanho da amostra $n$', fontsize=12)
ax2.set_ylabel('ISE (erro quadrático integrado)', fontsize=12)
ax2.set_title('Erro acumulado em todo o domínio vs. $n$\n'
              '(bandwidth pequeno → ISE estagna)', fontsize=12)
ax2.grid(True, which='both', alpha=0.3)
ax2.legend(fontsize=10)

plt.tight_layout()
plt.savefig('kde_ise_convergence.png', dpi=150, bbox_inches='tight')
plt.show()
