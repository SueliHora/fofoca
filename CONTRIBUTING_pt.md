# Guia de Contribuição — Fofoca Transcriptor

<p align="right">
  <a href="./CONTRIBUTING.md">[Read in English 🇺🇸]</a> | <b>Português 🇧🇷</b>
</p>

Obrigado pelo seu interesse em contribuir com o **Fofoca Transcriptor**! Aceitamos
contribuições da comunidade para otimizar desempenho, expandir suporte a modelos
neurais locais e aperfeiçoar a experiência de uso.

---

## 🔒 Diretriz Fundamental: Privacidade & Offline First (Air-Gapped)

O Fofoca Transcriptor é concebido desde a sua raiz como um **sistema 100% offline,
privado e air-gapped**. Para preservar a integridade e o propósito do projeto,
todas as contribuições devem seguir rigorosamente os seguintes princípios inegociáveis:

* **Execução 100% Local:** Todo o processamento de reconhecimento de fala
  (Whisper) e síntese de voz (Piper TTS) deve ocorrer exclusivamente em hardware
  local (CPU/GPU).
* **Zero Telemetria e Rastreamento:** A aplicação não deve enviar telemetria
  externa, métricas de uso, relatórios de crash ou analytics.
* **Nenhuma API Externa em Nuvem:** Pull Requests que introduzam consumo de
  APIs SaaS de terceiros, fallbacks remotos em nuvem, autenticação externa ou
  transmissão remota de dados **não** serão aceitos.

---

## 🛠 Fluxo de Contribuição

Siga os passos abaixo para contribuir de forma organizada:

### 1. Fork & Criação de Branch

Faça um fork do repositório no GitHub e crie uma branch específica para sua feature:

```bash
git checkout -b feature/nome-da-sua-feature
```

### 2. Configuração do Ambiente de Desenvolvimento

Você pode desenvolver e testar a aplicação localmente utilizando **Docker**
(recomendado para paridade imediata de ambiente) ou **uv**:

* **Opção A: Utilizando Docker (Rápido, ambiente isolado):**

  ```bash
  # Construir a imagem e iniciar o container
  docker compose up --build

  # Executar a suíte de testes dentro do container
  docker compose exec fofoca-app pytest -v
  ```

* **Opção B: Utilizando uv (Ambiente local):**

  Certifique-se de que Python 3.12+, `uv` e os binários de sistema `ffmpeg` e
  `espeak-ng` estão instalados, e então sincronize as dependências:

  ```bash
  uv sync --dev
  uv run python main.py
  ```

### 3. Linting, Formatação & Qualidade de Código

Verifique se as alterações respeitam os padrões de estilo do projeto executando
o linter estático e a checagem de formatação:

```bash
# Validação de regras de linting (Ruff)
uv run ruff check .

# Validação estrita de formatação (Ruff)
uv run ruff format --check .

# Auto-formatação automática de código (se necessário)
uv run ruff format .
```

### 4. Testes Automatizados

Execute a suíte de testes automatizados com `pytest` para garantir a integridade da aplicação:

```bash
uv run pytest -v
```

### 5. Envio do Pull Request & Preenchimento do Template

Envie sua branch para o seu fork no GitHub e abra um Pull Request apontando para
a branch `main`:

* **Preenchimento Completo do PR Template:** Certifique-se de preencher **todos**
  os campos do nosso [Template de Pull Request](.github/pull_request_template.md):
  * **Descrição das Mudanças:** Resumo claro do que foi implementado e justificativa.
  * **Issue Relacionada:** Vínculo com a issue abordada (ex: `Closes #12`).
  * **Tipo de Mudança:** Seleção das categorias correspondentes.
  * **Checklist do Contribuidor:** Confirmação de que lint, formatação, testes e
    a diretriz offline-first foram verificados.
  * **Screenshots / Validação:** Obrigatório para qualquer alteração na interface
    Gradio ou saída do terminal.
