# GitHub — como funciona

1. **Repo que te interessa → FORK no website** (cópia tua no GitHub)
   - Exemplo: https://github.com/statsmodels/statsmodels

2. **CLONE para o teu home folder** (cópia local no teu PC)
   ```bash
   git clone https://github.com/O-TEU-USERNAME/statsmodels.git
   ```

3. **Procuras issues** (ex: `good first issue`)
   - https://github.com/statsmodels/statsmodels/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22

4. **Resolves uma:**
   - a) editas o ficheiro localmente
   - b) no terminal:
     ```bash
     git add .
     git commit -m "mensagem descritiva"
     git push
     ```
     → envia para **O TEU fork**

5. **Abres um PULL REQUEST no website do GitHub:**
   > "ó repo original, aceitas as minhas mudanças?"
   - é aqui que os maintainers vêem, comentam e decidem

6. **PR aceite = MERGE ✅** | **PR recusado = fechas o PR ❌**
