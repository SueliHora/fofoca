# Contributing to Fofoca Transcriptor

Thank you for contributing to Fofoca Transcriptor! Please follow these streamlined steps to contribute:

1. **Fork & Branch:** Fork the repository and create your feature branch:

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Environment Setup:** Ensure Python 3.12+ and `uv` are installed, then install dependencies:

   ```bash
   uv sync --dev
   ```

3. **Linting & Code Quality:** Verify that your changes adhere to code style guidelines:

   ```bash
   uv run ruff check .
   ```

4. **Testing:** Run the automated test suite to ensure all checks pass:

   ```bash
   uv run pytest -v
   ```

5. **Submit Pull Request:** Push your branch to GitHub and open a Pull Request targeting the `main` branch with a clear summary of your changes.
