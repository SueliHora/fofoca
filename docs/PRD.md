# Product Requirements Document (PRD)

## Project: Fofoca Transcriptor
**Author & Lead Engineer:** Sueli da Hora Moreira  
**Status:** Approved / Production Ready  
**Target Version:** 1.0.0  
**Last Updated:** September 2026  

---

## 1. Executive Summary

**Fofoca Transcriptor** is an open-source, fully offline, privacy-first software suite designed for high-accuracy media transcription (Speech-to-Text) and neural speech synthesis (Text-to-Speech). Engineered to operate in air-gapped and resource-conscious environments, it eliminates external cloud dependencies, per-minute SaaS billing, upload bottlenecks, and corporate data leakage risks.

---

## 2. Problem Statement

Modern audio/video transcription and speech synthesis workflows are predominantly dominated by cloud-based SaaS providers (e.g., cloud Whisper APIs, Otter.ai, Descript, ElevenLabs). While convenient, these platforms present substantial operational and architectural bottlenecks:

1. **Restrictive File Size & Duration Limits:** Free or entry-level cloud services impose strict limits (e.g., 20–30 minutes per upload or maximum 25 MB payloads), failing completely on extensive technical lectures, meeting archives, and multi-hour educational sessions.
2. **Recurring Financial Costs:** Pay-as-you-go API tariffs scale linearly with audio duration, creating prohibitive ongoing expenses for students, independent researchers, and developers.
3. **Data Privacy & Compliance Risks:** Sensitive audio recordings (such as proprietary intellectual property, university lectures, medical discussions, or internal corporate meetings) sent to third-party cloud servers expose users to compliance violations (LGPD, GDPR) and privacy breaches.
4. **Network Dependency & Latency:** Uploading multi-gigabyte video or audio files over limited network bandwidth introduces massive latency and frequent transfer failures.

---

## 3. Target Audience & Value Proposition

### 3.1 Target Personas
* **Students & Researchers:** Requiring fast, cost-free transcription of 2+ hour recorded lectures, seminars, and interviews.
* **Software Engineers & Data Scientists:** Needing a modular, reproducible local pipeline that can be embedded into local RAG systems, agents, and data engineering pipelines.
* **Content Creators & Podcasters:** Converting draft scripts into natural speech or generating timestamped subtitles without SaaS subscription lock-in.
* **Privacy-Conscious Organizations:** Operating in air-gapped or strictly regulated environments where zero bytes of user data may leave the local network.

### 3.2 Value Proposition
* **Zero Cost & Infinite Scale:** Run unlimited hours of audio without recurring fees or subscription ceilings.
* **100% Data Confidentiality:** Audio processing, tensor calculations, and text generation happen strictly in local RAM and disk.
* **Turnkey Developer Experience:** Dual interface paradigm offering an elegant Gradio Web UI alongside decoupled CLI automation scripts.

---

## 4. Functional Requirements

### 4.1 Module 1: Automatic Speech Recognition (ASR / Audio-to-Text)
* **FR-1.1 (Multi-Format Media Ingestion):** Support standard audio (`.mp3`, `.wav`, `.m4a`, `.aac`) and video (`.mp4`, `.mkv`, `.mov`, `.avi`) container formats.
* **FR-1.2 (Model Tier Selection):** Allow dynamic selection between OpenAI Whisper model weights (`tiny`, `base`, `small`, `medium`, `large`) balancing speed versus accuracy.
* **FR-1.3 (Automated Language Detection):** Automatically detect spoken language across 90+ supported natural languages.
* **FR-1.4 (Timestamp Synchronization):** Extract segmented audio timestamps with clean `[MM:SS]` formatting for intuitive navigation.
* **FR-1.5 (Artifact Persistence & Export):** Automatically save timestamped transcripts to structured disk storage (`audio-to-text/output/`) and provide instantaneous clipboard copy and browser download.

### 4.2 Module 2: Neural Speech Synthesis (TTS / Text-to-Audio)
* **FR-2.1 (Raw Text Processing):** Ingest raw strings from direct user input or batch `.txt` files.
* **FR-2.2 (Neural Voice Selection):** Provide pre-configured, high-quality offline ONNX neural voices:
  * **Portuguese (pt_BR):** `pt_BR-faber-medium`
  * **English (en_US):** `en_US-lessac-medium`
* **FR-2.3 (Audio Generation):** Synthesize speech into standard `.wav` audio using optimized local ONNX runtime.
* **FR-2.4 (Playback & Export):** Provide an embedded web player for instantaneous auditioning and direct file download.

### 4.3 Module 3: User Interface & Entrypoints
* **FR-3.1 (Interactive Web Application):** High-productivity browser UI built with Gradio Blocks, styled with a modern, responsive theme.
* **FR-3.2 (Decoupled CLI Automation):** Standalone command-line scripts (`transcriber.py` and `speaker.py`) enabling headless batch processing.
* **FR-3.3 (Unified Launcher):** Single-command root entrypoints (`python app.py` and `python main.py`).

---

## 5. Non-Functional Requirements

### 5.1 Security, Privacy & Air-Gap Compliance
* **NFR-1.1 (Zero Outbound Telemetry):** The software must perform zero outbound network requests during inference. All weights, models, and dependencies must resolve locally.
* **NFR-1.2 (Local Data Lifecycle):** Raw inputs and generated outputs remain stored exclusively within the user's workspace directory.

### 5.2 Performance & Resource Management
* **NFR-2.1 (Model Caching):** Implement in-memory model caching to avoid expensive reload latencies across repeated user requests.
* **NFR-2.2 (Hardware Acceleration):** Utilize PyTorch and ONNX Runtime backends capable of leveraging CUDA/ROCm when available, with seamless fallback to CPU vector execution.

### 5.3 Modern Tooling & Packaging
* **NFR-3.1 (Deterministic Dependency Resolution):** Fully integrated with `uv` for ultra-fast lockfile resolution, virtual environment provisioning, and reproducible builds.
* **NFR-3.2 (Standard Compliance):** Comply with PEP 517, PEP 518, and PEP 621 specifications via `pyproject.toml`.

### 5.4 Maintainability & Quality Assurance
* **NFR-4.1 (Unit Testing Suite):** Test coverage verifying directory structural integrity, module importability, and model mapping configurations via `pytest`.
* **NFR-4.2 (Continuous Integration):** Automated GitHub Actions pipeline executing dependency validation and test suites on every pull request and push to `main`.
