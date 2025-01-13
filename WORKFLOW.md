
# Passo a Passo para Trabalhar no Projeto Jornaleiro

## **A. Início da Sessão**

### **1. Abrir o Projeto no VS Code**
1. Abra o VS Code.
2. Navegue até o diretório do projeto:
   - Atalho: `Ctrl+O` (ou `Cmd+O` no macOS) e selecione a pasta do projeto.
   - Ou use o terminal:
     ```bash
     code /caminho/para/seu/projeto
     ```

### **2. Ativar o Ambiente Conda**
1. Abra o terminal integrado no VS Code (`Ctrl+\`` ou `Cmd+\`` no macOS).
2. Ative o ambiente Conda:
   ```bash
   conda activate jornaleiro
   ```
3. Confirme se o ambiente foi ativado verificando o prefixo `(jornaleiro)` no terminal.

### **3. Sincronizar com o Repositório no GitHub**
1. **Verificar mudanças no repositório remoto**:
   ```bash
   git fetch
   ```
2. **Atualizar o repositório local**:
   ```bash
   git pull origin main
   ```
   - Substitua `main` pelo nome correto do branch, se necessário.

3. **Resolução de conflitos** (se aplicável):
   - Resolva os conflitos manualmente no editor ou terminal.
   - Após resolver, finalize o merge:
     ```bash
     git add .
     git commit -m "Conflitos resolvidos"
     ```

### **4. Verificar Dependências**
1. Verifique se todas as dependências estão instaladas:
   ```bash
   pip list
   ```
2. Instale dependências ausentes (se necessário):
   ```bash
   pip install -r requirements.txt
   ```

---

## **B. Durante a Sessão**

### **1. Trabalhar no Projeto**
1. Certifique-se de que o interpretador Python está configurado corretamente:
   - No VS Code, pressione `Ctrl+Shift+P` (ou `Cmd+Shift+P` no macOS) e selecione **Python: Select Interpreter**.
   - Escolha o ambiente Conda (`jornaleiro`).

2. Faça alterações no código conforme necessário.

3. Teste o projeto:
   - Execute o servidor local:
     ```bash
     uvicorn main:app --reload
     ```
   - Acesse [http://127.0.0.1:8000](http://127.0.0.1:8000) no navegador.

### **2. Testar Funcionalidades**
1. Use o terminal para rodar testes automatizados:
   ```bash
   pytest
   ```

---

## **C. Finalização da Sessão**

### **1. Verificar Alterações no Git**
1. Confira o status do repositório local:
   ```bash
   git status
   ```
2. Adicione as alterações:
   ```bash
   git add .
   ```
3. Faça um commit com uma mensagem descritiva:
   ```bash
   git commit -m "Descrição das alterações realizadas"
   ```

4. Envie as alterações para o GitHub:
   ```bash
   git push origin main
   ```

### **2. Encerrar o Ambiente**
1. Desative o ambiente Conda:
   ```bash
   conda deactivate
   ```

2. Salve todas as abas abertas no VS Code e feche o editor.

---

## **D. Checklist Resumido**

### **No Início da Sessão**
- [ ] Abra o projeto no VS Code.
- [ ] Ative o ambiente Conda com `conda activate jornaleiro`.
- [ ] Sincronize com o repositório remoto usando `git pull`.
- [ ] Verifique se todas as dependências estão instaladas.

### **Durante a Sessão**
- [ ] Faça alterações e implemente novas funcionalidades.
- [ ] Teste o código e o servidor local.

### **No Final da Sessão**
- [ ] Verifique as alterações no Git com `git status`.
- [ ] Adicione, commit e envie alterações ao GitHub (`git add .`, `git commit -m`, `git push`).
- [ ] Desative o ambiente Conda com `conda deactivate`.
