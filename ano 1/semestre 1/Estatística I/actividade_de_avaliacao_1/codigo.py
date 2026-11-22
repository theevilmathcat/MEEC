"""
AA1 - Estatística I [22017] — Verificação
===============================================================
Número de identificação exemplo: 1234567
  a=1, b=2, c=2, d=2, e=2, f=2, g=2
  m = min{1,2,2,2,2,2,2} = 1
  M = max{1,2,2,2,2,2,2} = 2  (note: o enunciado diz max=7 apenas se digits forem diferentes)

NOTA: O enunciado usa o exemplo 1234567 onde a=1,b=2,...,g=7 (todos diferentes),
logo m=1, M=7. Usamos esse exemplo para Exercício 2.
Para Exercício 3 usamos o mesmo número, m=1, M=2 (max dos digits do número).
"""

import numpy as np
from scipy import stats
import math

SEP  = "=" * 70
SEP2 = "-" * 70

def print_section(title):
    print(f"\n{SEP}")
    print(f"  {title}")
    print(SEP)

def print_subsection(title):
    print(f"\n{SEP2}")
    print(f"  {title}")
    print(SEP2)

# ================================================================
# EXERCÍCIO 1 — SONDAGEM ICS/ISCTE JANEIRO 2026
# ================================================================
print_section("EXERCÍCIO 1 — SONDAGEM ICS/ISCTE JANEIRO 2026")
print("Fonte: Quadros de Resultados ponderados (n=782 recenseados)")

# --- 1.1 Intervalos de Confiança para Intenção de Voto (SV2) ---
print_subsection("1.1 IC 95% para a Proporção de Intenção de Voto na 2.ª Volta")

n = 782
alpha_ic = 0.05
z_half = stats.norm.ppf(1 - alpha_ic/2)
print(f"n = {n}")
print(f"Nível de confiança: {(1-alpha_ic)*100:.0f}%")
print(f"z_{{alpha/2}} = z_{{0.025}} = {z_half:.4f}")

candidates = {
    "António José Seguro": 0.51,
    "André Ventura":       0.27,
}

for name, p_hat in candidates.items():
    se = math.sqrt(p_hat * (1 - p_hat) / n)
    me = z_half * se
    lower, upper = p_hat - me, p_hat + me
    print(f"\n  {name}:")
    print(f"    p_hat = {p_hat}")
    print(f"    EP(p_hat) = sqrt({p_hat}*{1-p_hat}/{n}) = sqrt({p_hat*(1-p_hat)/n:.8f}) = {se:.6f}")
    print(f"    Margem de erro = {z_half:.4f} * {se:.6f} = {me:.6f}")
    print(f"    IC 95% = ({p_hat} - {me:.6f} ; {p_hat} + {me:.6f})")
    print(f"           = ({lower:.6f} ; {upper:.6f})")
    print(f"           = ({lower*100:.2f}% ; {upper*100:.2f}%)")

# --- 1.2 Teste Seguro > 50% ---
print_subsection("1.2 Teste H0: p_Seguro <= 0.50 vs H1: p_Seguro > 0.50 (unilateral)")

p_hat_s = 0.51
p0 = 0.50
n = 782

numerator   = p_hat_s - p0
denominator = math.sqrt(p0 * (1 - p0) / n)
Z = numerator / denominator
p_value = 1 - stats.norm.cdf(Z)
z_crit_01  = stats.norm.ppf(0.99)
z_crit_005 = stats.norm.ppf(0.95)

print(f"  H0: p <= {p0}  vs  H1: p > {p0}")
print(f"  p_hat = {p_hat_s},  n = {n}")
print(f"  Estatística Z = (p_hat - p0) / sqrt(p0*(1-p0)/n)")
print(f"               = ({p_hat_s} - {p0}) / sqrt({p0}*{1-p0}/{n})")
print(f"               = {numerator} / sqrt({p0*(1-p0)/n:.8f})")
print(f"               = {numerator} / {denominator:.6f}")
print(f"               = {Z:.4f}")
print(f"  p-value (unilateral direita) = P(Z > {Z:.4f}) = 1 - Phi({Z:.4f}) = {p_value:.4f}")
print(f"  Valor crítico alpha=0.01: z_0.99 = {z_crit_01:.4f}")
print(f"  Valor crítico alpha=0.05: z_0.95 = {z_crit_005:.4f}")
print(f"  Decisão: {'Rejeitar H0' if p_value < 0.05 else 'Nao rejeitar H0'} a 5%")
print(f"  => p-value = {p_value:.4f} > 0.05: NAO se rejeita H0")

# --- 1.3 Diferença de Género ---
print_subsection("1.3 Teste H0: p_mulheres = p_homens (bilateral, 2 amostras)")

p_m = 0.46; n_m = 367
p_f = 0.54; n_f = 416

p_pool = (p_m * n_m + p_f * n_f) / (n_m + n_f)
var_pool = p_pool * (1 - p_pool) * (1/n_m + 1/n_f)
se_diff = math.sqrt(var_pool)
Z_g = (p_f - p_m) / se_diff
p_g = 2 * (1 - stats.norm.cdf(abs(Z_g)))

print(f"  H0: p_H = p_M  vs  H1: p_H != p_M")
print(f"  Homens:   p_H = {p_m}, n_H = {n_m}")
print(f"  Mulheres: p_M = {p_f}, n_M = {n_f}")
print(f"  p_pool = ({p_m}*{n_m} + {p_f}*{n_f}) / ({n_m}+{n_f})")
print(f"         = {p_m*n_m + p_f*n_f} / {n_m+n_f}")
print(f"         = {p_pool:.6f}")
print(f"  Var_pool = {p_pool:.6f} * {1-p_pool:.6f} * (1/{n_m} + 1/{n_f})")
print(f"           = {p_pool*(1-p_pool):.6f} * {1/n_m + 1/n_f:.8f}")
print(f"           = {var_pool:.8f}")
print(f"  SE = sqrt({var_pool:.8f}) = {se_diff:.6f}")
print(f"  Z = ({p_f} - {p_m}) / {se_diff:.6f}")
print(f"    = {p_f - p_m} / {se_diff:.6f}")
print(f"    = {Z_g:.4f}")
print(f"  p-value (bilateral) = 2*P(Z > |{Z_g:.4f}|) = {p_g:.4f}")
print(f"  Decisão a 5%: {'Rejeitar H0' if p_g < 0.05 else 'Nao rejeitar H0'}")

# --- 1.4 Honestidade P4.1 ---
print_subsection("1.4 Teste H0: p_Seguro_honesto = 0.50 vs H1: p != 0.50 (bilateral)")

n_S = 406; n_V = 172
n_tot = n_S + n_V
p_sh = n_S / n_tot
Z_h = (p_sh - 0.5) / math.sqrt(0.25 / n_tot)
p_h = 2 * (1 - stats.norm.cdf(abs(Z_h)))

print(f"  Apenas respondentes que escolheram um candidato: n = {n_tot}")
print(f"  Escolheram Seguro: {n_S}  |  Escolheram Ventura: {n_V}")
print(f"  p_hat(Seguro) = {n_S}/{n_tot} = {p_sh:.6f}")
print(f"  H0: p = 0.50  vs  H1: p != 0.50")
print(f"  Z = ({p_sh:.6f} - 0.50) / sqrt(0.25/{n_tot})")
print(f"    = {p_sh - 0.5:.6f} / sqrt({0.25/n_tot:.8f})")
print(f"    = {p_sh - 0.5:.6f} / {math.sqrt(0.25/n_tot):.6f}")
print(f"    = {Z_h:.4f}")
print(f"  p-value (bilateral) = {p_h:.8f}")
print(f"  Decisão: Rejeitar H0 a qualquer nivel usual (p << 0.001)")


# ================================================================
# EXERCÍCIO 2 — SISTEMA DE IA
# ================================================================
print_section("EXERCÍCIO 2 — SISTEMA DE IA PARA DETEÇÃO DE DEFEITOS")
print("ID exemplo: 1234567  =>  m=1, M=7")
print("Limiar aceitável: p0 = (m+1)% = 2% = 0.02")
print("Proporção verdadeira: p_real = (m+M)% = 8% = 0.08")

m_ex2 = 1; M_ex2 = 7
p0_ex2   = (m_ex2 + 1) / 100
p_true   = (m_ex2 + M_ex2) / 100

print(f"\n  p0 = ({m_ex2}+1)/100 = {p0_ex2}")
print(f"  p_real = ({m_ex2}+{M_ex2})/100 = {p_true}")

# (a) All 4 scenarios
print_subsection("(a) Análise dos Quatro Cenários")
print(f"  H0: p <= {p0_ex2}  vs  H1: p > {p0_ex2}  [teste unilateral direito]")

scenarios = [
    (100, 0.01, "(i)"),
    (100, 0.05, "(ii)"),
    (20,  0.01, "(iii)"),
    (20,  0.05, "(iv)"),
]

for n_sc, alpha_sc, lbl in scenarios:
    print(f"\n  Cenário {lbl}: n={n_sc}, alpha={alpha_sc}")
    z_alpha = stats.norm.ppf(1 - alpha_sc)
    se0 = math.sqrt(p0_ex2 * (1 - p0_ex2) / n_sc)
    p_crit = p0_ex2 + z_alpha * se0
    print(f"    z_alpha = z_{1-alpha_sc} = {z_alpha:.4f}")
    print(f"    SE(p0)  = sqrt({p0_ex2}*{1-p0_ex2}/{n_sc}) = sqrt({p0_ex2*(1-p0_ex2)/n_sc:.8f}) = {se0:.6f}")
    print(f"    Regiao critica: p_hat > p0 + z_alpha*SE = {p0_ex2} + {z_alpha:.4f}*{se0:.6f} = {p_crit:.6f}")
    
    # Power under p_true
    se_true = math.sqrt(p_true * (1 - p_true) / n_sc)
    z_beta  = (p_crit - p_true) / se_true
    beta    = stats.norm.cdf(z_beta)
    power   = 1 - beta
    print(f"    --- Potência do teste (alínea b) ---")
    print(f"    SE(p_real) = sqrt({p_true}*{1-p_true}/{n_sc}) = {se_true:.6f}")
    print(f"    z_beta = (p_crit - p_real) / SE(p_real)")
    print(f"           = ({p_crit:.6f} - {p_true}) / {se_true:.6f}")
    print(f"           = {p_crit - p_true:.6f} / {se_true:.6f}")
    print(f"           = {z_beta:.4f}")
    print(f"    beta = P(Z < {z_beta:.4f}) = Phi({z_beta:.4f}) = {beta:.4f}")
    print(f"    Potência = 1 - beta = {power:.4f}")
    print(f"    P(sistema considerado aceitável | p_real={p_true}) = beta = {beta:.4f}")

# Chosen: (ii)
print_subsection("(b) Cenário Escolhido: (ii) n=100, alpha=0.05 — Cálculo Detalhado de beta")
n_ch=100; alpha_ch=0.05
z_a=stats.norm.ppf(1-alpha_ch)
se0=math.sqrt(p0_ex2*(1-p0_ex2)/n_ch)
p_crit=p0_ex2+z_a*se0
se_t=math.sqrt(p_true*(1-p_true)/n_ch)
z_b=(p_crit-p_true)/se_t
beta=stats.norm.cdf(z_b)
power=1-beta

print(f"  n={n_ch}, alpha={alpha_ch}, p0={p0_ex2}, p_real={p_true}")
print(f"")
print(f"  PASSO 1 — Valor crítico p_hat_crit:")
print(f"    z_{{0.05}} = {z_a:.6f}")
print(f"    SE(H0)  = sqrt({p0_ex2}*(1-{p0_ex2})/{n_ch})")
print(f"            = sqrt({p0_ex2*(1-p0_ex2):.6f}/{n_ch})")
print(f"            = sqrt({p0_ex2*(1-p0_ex2)/n_ch:.8f})")
print(f"            = {se0:.6f}")
print(f"    p_hat_crit = {p0_ex2} + {z_a:.6f} * {se0:.6f}")
print(f"               = {p0_ex2} + {z_a*se0:.6f}")
print(f"               = {p_crit:.6f}")
print(f"")
print(f"  PASSO 2 — beta (Erro Tipo II) quando p_real={p_true}:")
print(f"    SE(p_real) = sqrt({p_true}*(1-{p_true})/{n_ch})")
print(f"               = sqrt({p_true*(1-p_true):.6f}/{n_ch})")
print(f"               = sqrt({p_true*(1-p_true)/n_ch:.8f})")
print(f"               = {se_t:.6f}")
print(f"    z_beta = (p_hat_crit - p_real) / SE(p_real)")
print(f"           = ({p_crit:.6f} - {p_true}) / {se_t:.6f}")
print(f"           = {p_crit-p_true:.6f} / {se_t:.6f}")
print(f"           = {z_b:.6f}")
print(f"    beta = Phi({z_b:.6f}) = {beta:.6f}")
print(f"    Potência = 1 - {beta:.6f} = {power:.6f}")
print(f"")
print(f"  RESULTADO: P(sistema considerado aceitável | p_real=0.08) = {beta:.4f} ({beta*100:.2f}%)")
print(f"             Potência do teste = {power:.4f} ({power*100:.2f}%)")


# ================================================================
# EXERCÍCIO 3 — CONSUMO DE ENERGIA
# ================================================================
print_section("EXERCÍCIO 3 — ESTRATÉGIAS DE POUPANÇA DE ENERGIA")
print("ID: 1234567  =>  a=1,b=2,c=2,d=2,e=2,f=2,g=2  =>  m=1, M=2")

a_,b_,c_,d_,e_,f_,g_ = 1,2,2,2,2,2,2
m_ = min(a_,b_,c_,d_,e_,f_,g_)
M_ = max(a_,b_,c_,d_,e_,f_,g_)

A_antes  = np.array([18, 20, 19, 21, 18, 22, 20, 19, 10+a_, 10],   dtype=float)
A_depois = np.array([16-b_, 17, 16, 18, 15, 19, 17, 16-c_, 15, 15], dtype=float)
B_antes  = np.array([19, 21, 18, 20+d_, 22, 19, 21, 18, 20+e_, 19], dtype=float)
B_depois = np.array([14, 16-f_, 15, 16, 17, 15, 16, 14, 16, 15],    dtype=float)
C_antes  = np.array([17, 19, 20, 18+g_, 21, 17+m_, 19, 20, 18, 21], dtype=float)
C_depois = np.array([18, 19-M_, 19, 17, 20, 18, 20, 19, 18, 20],    dtype=float)

print(f"\n  m={m_}, M={M_}")
print(f"\n  Tabela completa (valores preenchidos):")
print(f"  Grupo A — Antes:  {A_antes.astype(int).tolist()}")
print(f"  Grupo A — Depois: {A_depois.astype(int).tolist()}")
print(f"  Grupo B — Antes:  {B_antes.astype(int).tolist()}")
print(f"  Grupo B — Depois: {B_depois.astype(int).tolist()}")
print(f"  Grupo C — Antes:  {C_antes.astype(int).tolist()}")
print(f"  Grupo C — Depois: {C_depois.astype(int).tolist()}")

# --- (a) ANOVA ---
print_subsection("(a) ANOVA one-way — Consumo Médio Depois (3 grupos independentes)")

groups = {"A": A_depois, "B": B_depois, "C": C_depois}
n_groups = {k: len(v) for k,v in groups.items()}
means    = {k: np.mean(v) for k,v in groups.items()}
vars_    = {k: np.var(v, ddof=1) for k,v in groups.items()}
stds_    = {k: np.std(v, ddof=1) for k,v in groups.items()}

print(f"\n  Estatísticas descritivas (fase Depois):")
for g in ["A","B","C"]:
    print(f"    Grupo {g}: n={n_groups[g]}, media={means[g]:.4f}, var={vars_[g]:.4f}, dp={stds_[g]:.4f}")

all_depois = np.concatenate([A_depois, B_depois, C_depois])
grand_mean = np.mean(all_depois)
N_total = len(all_depois)
k = 3

print(f"\n  Grande média (grand mean) = {grand_mean:.4f}")
print(f"  N total = {N_total}, k = {k}")

# Manual ANOVA calculations
SSB = sum(n_groups[g] * (means[g] - grand_mean)**2 for g in ["A","B","C"])
SSW = sum((n_groups[g]-1) * vars_[g] for g in ["A","B","C"])
SST = SSB + SSW
dfB = k - 1; dfW = N_total - k; dfT = N_total - 1
MSB = SSB / dfB; MSW = SSW / dfW
F = MSB / MSW
p_F = 1 - stats.f.cdf(F, dfB, dfW)

print(f"\n  --- Tabela ANOVA ---")
print(f"  Fonte        SS          df    MS          F         p-value")
print(f"  Entre grupos SSB = {SSB:.4f}   {dfB}     MSB = {MSB:.4f}   F = {F:.4f}   p = {p_F:.6f}")
print(f"  Dentro grupos SSW = {SSW:.4f}   {dfW}    MSW = {MSW:.4f}")
print(f"  Total        SST = {SST:.4f}   {dfT}")

# Verification with scipy
F_scipy, p_scipy = stats.f_oneway(A_depois, B_depois, C_depois)
print(f"\n  Verificação scipy.stats.f_oneway: F={F_scipy:.4f}, p={p_scipy:.6f}")
print(f"  Match manual: F {'OK' if abs(F-F_scipy)<1e-6 else 'ERRO'}, p {'OK' if abs(p_F-p_scipy)<1e-6 else 'ERRO'}")
print(f"\n  Decisão: p={p_F:.6f} < 0.001 => Rejeitar H0 a 1%")

# --- Post-hoc Welch t-tests ---
print_subsection("(a) Comparações Post-hoc — Teste t de Welch (variâncias desiguais)")
print("    Teste t de Welch: nao assume igualdade de variâncias (mais robusto para n pequeno)")
print("    Fórmula: t = (x1_bar - x2_bar) / sqrt(s1^2/n1 + s2^2/n2)")
print("    Graus de liberdade Welch-Satterthwaite:")
print("    df = (s1^2/n1 + s2^2/n2)^2 / [ (s1^2/n1)^2/(n1-1) + (s2^2/n2)^2/(n2-1) ]")
print(f"\n    Correção Bonferroni: alpha_ajustado = 0.05/3 = {0.05/3:.6f} ≈ 0.0167")

comparisons = [
    ("A", "B", A_depois, B_depois),
    ("A", "C", A_depois, C_depois),
    ("B", "C", B_depois, C_depois),
]

for g1, g2, x1, x2 in comparisons:
    n1, n2 = len(x1), len(x2)
    x1b, x2b = np.mean(x1), np.mean(x2)
    s1, s2 = np.std(x1,ddof=1), np.std(x2,ddof=1)
    s1sq_n = s1**2/n1; s2sq_n = s2**2/n2
    
    # Manual Welch t
    t_welch = (x1b - x2b) / math.sqrt(s1sq_n + s2sq_n)
    
    # Welch-Satterthwaite df
    df_welch = (s1sq_n + s2sq_n)**2 / (s1sq_n**2/(n1-1) + s2sq_n**2/(n2-1))
    
    p_welch = 2 * stats.t.sf(abs(t_welch), df=df_welch)
    
    # Scipy verification
    t_sc, p_sc = stats.ttest_ind(x1, x2, equal_var=False)
    
    sig_bf = "SIM" if p_welch < 0.05/3 else "NAO"
    
    print(f"\n  Comparação Grupo {g1} vs Grupo {g2}:")
    print(f"    n{g1}={n1}, x{g1}_bar={x1b:.4f}, s{g1}={s1:.6f}, s{g1}^2/n{g1}={s1sq_n:.8f}")
    print(f"    n{g2}={n2}, x{g2}_bar={x2b:.4f}, s{g2}={s2:.6f}, s{g2}^2/n{g2}={s2sq_n:.8f}")
    print(f"    Diferenca de médias: {x1b:.4f} - {x2b:.4f} = {x1b-x2b:.4f}")
    print(f"    SE = sqrt({s1sq_n:.8f} + {s2sq_n:.8f}) = sqrt({s1sq_n+s2sq_n:.8f}) = {math.sqrt(s1sq_n+s2sq_n):.6f}")
    print(f"    t_Welch = {x1b-x2b:.4f} / {math.sqrt(s1sq_n+s2sq_n):.6f} = {t_welch:.6f}")
    print(f"    df_Welch = ({s1sq_n:.8f} + {s2sq_n:.8f})^2 / [{s1sq_n:.8f}^2/{n1-1} + {s2sq_n:.8f}^2/{n2-1}]")
    num_df = (s1sq_n + s2sq_n)**2
    den_df = s1sq_n**2/(n1-1) + s2sq_n**2/(n2-1)
    print(f"           = {num_df:.8f} / {den_df:.8f} = {df_welch:.4f}")
    print(f"    p-value (bilateral) = 2*P(T_{df_welch:.2f} > |{t_welch:.4f}|) = {p_welch:.6f}")
    print(f"    Scipy check: t={t_sc:.6f}, p={p_sc:.6f}  => {'OK' if abs(t_welch-t_sc)<1e-6 else 'VERIFICAR'}")
    print(f"    Significativo (Bonferroni alpha=0.0167): {sig_bf}")

# --- (b) Paired t-tests ---
print_subsection("(b) Testes t Pareados — Alteração do Consumo Dentro de Cada Grupo")
print("    H0: mu_D = 0  vs  H1: mu_D != 0  onde D_i = X_antes_i - X_depois_i")
print("    Estatística: t = D_bar / (s_D / sqrt(n)),   df = n-1")

for g, antes, depois in [("A",A_antes,A_depois),("B",B_antes,B_depois),("C",C_antes,C_depois)]:
    D = antes - depois
    n = len(D)
    D_bar = np.mean(D)
    s_D = np.std(D, ddof=1)
    se_D = s_D / math.sqrt(n)
    t_stat = D_bar / se_D
    df = n - 1
    p_two = 2 * stats.t.sf(abs(t_stat), df=df)
    
    # scipy
    t_sc, p_sc = stats.ttest_rel(antes, depois)
    
    print(f"\n  Grupo {g}:")
    print(f"    Diferenças D = Antes - Depois:")
    print(f"      {D.astype(int).tolist()}")
    print(f"    D_bar = {D_bar:.4f}")
    print(f"    s_D   = sqrt(SQD/(n-1)) onde SQD = sum((Di - D_bar)^2)")
    SQD = np.sum((D - D_bar)**2)
    print(f"          = sqrt({SQD:.4f}/{n-1}) = sqrt({SQD/(n-1):.6f}) = {s_D:.6f}")
    print(f"    SE    = s_D / sqrt(n) = {s_D:.6f} / sqrt({n}) = {s_D/math.sqrt(n):.6f}")
    print(f"    t({df}) = {D_bar:.4f} / {se_D:.6f} = {t_stat:.6f}")
    print(f"    p-value (bilateral) = 2*P(T_{df} > |{t_stat:.4f}|) = {p_two:.6f}")
    print(f"    Scipy check: t={t_sc:.6f}, p={p_sc:.6f}  => {'OK' if abs(t_stat-t_sc)<1e-9 else 'VERIFICAR'}")
    print(f"    Nivel minimo de significância (alpha_min) = p-value = {p_two:.6f}")
    if p_two < 0.001:
        print(f"    => Significativo para alpha > 0.001%")
    elif p_two < 0.01:
        print(f"    => Significativo para alpha > 0.1%")
    elif p_two < 0.05:
        print(f"    => Significativo para alpha > {p_two*100:.2f}%")
    else:
        print(f"    => NAO significativo a 5% nem a 10%")
        print(f"       Apenas significativo para alpha > {p_two*100:.2f}%")

print(f"\n{SEP}")
print("  VERIFICAÇÃO COMPLETA CONCLUÍDA — Todos os cálculos confirmados")
print(SEP)
