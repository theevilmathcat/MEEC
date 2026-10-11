# README — KDE Bandwidth Visualiser

## Overview

This script demonstrates **Kernel Density Estimation (KDE)** and the critical role that **bandwidth selection** plays in recovering an unknown probability density from samples. It uses a synthetic bimodal distribution (a mixture of two Gaussians) as the ground truth and shows, across four sample sizes, how three different fixed bandwidths produce under-smoothed, well-smoothed, and over-smoothed estimates. A second analysis quantifies estimation error numerically using the **Integrated Squared Error (ISE)** and plots how each bandwidth's error decays (or stalls) as the sample size grows.

## Features

- Visual comparison of three bandwidths (`h = 0.05`, `0.30`, `1.50`) across four sample sizes (`n = 20, 100, 500, 5000`)
- Overlay of the true density, histogram, and KDE curves on each panel
- ISE convergence plot on a log-log scale with mean ± standard deviation bands (averaged over 30 repetitions per sample size)
- Reference `1/n` decay line to benchmark bandwidth performance
- Outputs two publication-quality PNG figures at 150 dpi

## Requirements

```
python >= 3.8
numpy
matplotlib
scipy
```

Install all dependencies with:

```bash
pip install numpy matplotlib scipy
```

## Usage

```bash
python kde_bandwidth.py
```

No arguments are required. The script runs end-to-end and saves two figures to the current working directory. The random seed is fixed (`np.random.seed(42)`) so results are fully reproducible.

## Outputs

| File | Description |
| --- | --- |
| `kde_bandwidth.png` | 2×2 grid showing KDE estimates vs. true density for each of the four sample sizes |
| `kde_ise_convergence.png` | Log-log plot of mean ISE vs. sample size `n` for each bandwidth, with ±1 std bands |

## Background

Kernel Density Estimation is a non-parametric method for estimating a probability density function from data. The **bandwidth** `h` controls the bias-variance trade-off:

- **Too small** (`h = 0.05`): the estimate is noisy and spiky — high variance, low bias. ISE stagnates as `n` grows because the variance cannot average away.
- **Well-chosen** (`h = 0.30`): the estimate tracks the true bimodal shape closely and ISE falls steadily with more data, approaching the optimal `O(1/n)` rate.
- **Too large** (`h = 1.50`): the estimate is over-smoothed — the two modes merge into one broad bump. ISE is dominated by bias and also stops improving with larger samples.

The ISE convergence plot makes this concrete: only the correctly-sized bandwidth achieves a decay rate close to `1/n` on the log-log scale. The labels in the script are in Portuguese (`h = 0.30 (adequado)` = "appropriate"), reflecting its original educational context.
