# Contributing to Fofoca Transcriptor

<p align="right">
  <b>English 🇺🇸</b> | <a href="./CONTRIBUTING_pt.md">[Leia em Português 🇧🇷]</a>
</p>

Thank you for your interest in contributing to **Fofoca Transcriptor**! We welcome
community contributions to enhance performance, expand local model capabilities,
and refine user experience.

---

## 🔒 Core Guideline: Privacy & Offline First (Air-Gapped)

Fofoca Transcriptor is fundamentally engineered as an **offline, private,
air-gapped system**. To protect the integrity and founding mission of the project,
all contributions must strictly respect these non-negotiable principles:

* **100% Local Execution:** All speech recognition (Whisper) and speech
  synthesis (Piper TTS) inference must execute entirely on local hardware (CPU/GPU).
* **Zero Telemetry & Tracking:** The application must never emit outbound network
  telemetry, usage metrics, crash reports, or analytics.
* **No External Cloud APIs:** Pull requests introducing third-party SaaS APIs,
  remote cloud fallbacks, remote authentication, or external data transmission
  will **not** be accepted.

---

## 🛠 Contribution Workflow

Please follow these streamlined steps to contribute:

### 1. Fork & Branch

Fork the repository on GitHub and create a dedicated feature branch:

```bash
git checkout -b feature/your-feature-name
```

### 2. Environment Setup

You can develop and test the application locally using either **Docker**
(recommended for zero-setup environment parity) or **uv**:

* **Option A: Using Docker (Fastest, isolated environment):**

  ```bash
  # Build and start the container
  docker compose up --build

  # Run test suite inside container
  docker compose exec fofoca-app pytest -v
  ```

* **Option B: Using uv (Local environment):**

  Ensure Python 3.12+, `uv`, and system packages for `ffmpeg` and
  `espeak-ng` are installed, then sync dependencies:

  ```bash
  uv sync --dev
  uv run python main.py
  ```

### 3. Linting, Formatting & Code Quality

Verify that your changes adhere to code style guidelines and pass both static
analysis and format checks:

```bash
# Verify linting rules (Ruff)
uv run ruff check .

# Verify code formatting (Ruff)
uv run ruff format --check .

# Automatically apply formatting fixes if needed
uv run ruff format .
```

### 4. Automated Testing

Run the full automated test suite to ensure all unit and integration checks pass:

```bash
uv run pytest -v
```

### 5. Submit Pull Request & Complete Template

Push your branch to your GitHub fork and open a Pull Request targeting the
`main` branch:

* **Complete the PR Template:** Make sure to fill out **all** sections of our
  [Pull Request Template](.github/pull_request_template.md), including:
  * **Description of Changes:** Clear summary of what was changed and why.
  * **Related Issue:** Link to the relevant issue (e.g., `Closes #12`).
  * **Type of Change:** Select the appropriate category tags.
  * **Contributor Checklist:** Verify all verification items (lint, format,
    offline-first guarantee, test passing).
  * **Screenshots / Validation:** Required for any modifications touching the
    Gradio Web UI or CLI output.
