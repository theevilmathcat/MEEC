# GitHub — como funciona em 7 passos

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

7. ## Branches e PRs — o que é isto?

- **Branch** = linha de trabalho paralela. O `main` é a versão "oficial".
- Crias um branch novo para mexer **sem estragar o `main`**.
- No GitHub (a editar pelo website) aparece uma caixa com 2 opções:
  - ○ Commit directly to `main` → mete a mudança logo no main (simples, mas suja)
  - ● **Create a new branch for this commit and start a pull request** → cria branch + commit + abre PR **num clique só**
- **Para contribuir (statsmodels, etc.) → usa a opção 2, sempre.**
- **Para o teu próprio repo (ex: notas) → `main` direto é na boa.** Não há PR para ninguém.

### Website vs Terminal (mesma coisa, ferramentas diferentes)

| | Website | Terminal |
|---|---|---|
| Criar branch | clicas na caixa | `git checkout -b nome` |
| Commit | "Commit changes" | `git commit -m "..."` |
| PR | clique automático | abres no website à mão |

Regra para guardar seja o que fôr de ficheiros: branch = ramo separado; main = tronco. 

Não se mexe no tronco directamente quando estás a contribuir para algo que não é teu ou que queres verificar primeiasdasdrmeiro

