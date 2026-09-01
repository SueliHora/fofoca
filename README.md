<div align="center">
  <img src="./logo.png" alt="Fofoca Transcriptor Logo" width="200">
  <h1>🦭 Fofoca Transcriptor</h1>
  <p><b>A 100% offline, local, free, and smart ecosystem for audio, video, and text processing.</b></p>
  <p><i>Created by <b>Sueli da Hora Moreira</b></i></p>
  <p>Designed for productivity, privacy, autonomy, and language studies without paywalls or size limits.</p>
</div>

---

## 📖 The Origin Story

This project was not born in a classroom or from a generic tutorial. It was built to solve a real-world bottleneck: after missing a critical 2-hour lecture on RAG (Retrieval-Augmented Generation) and LLMs, I faced a series of classic infrastructure walls:

* No free online transcription service accepted a file of that duration and size.
* When I tried splitting the audio, I immediately hit restrictive daily processing limits.
* Paid transcription tools were outside my budget for a personal study need.

So I built my own solution — **open source, local, private, and completely free of arbitrary limits**.

Later, I expanded the ecosystem to include text-to-speech synthesis for studying English pronunciation and listening to materials on the go. **Fofoca Transcriptor** is the result: a personal, modular toolkit for audio processing designed for total autonomy.

---

## 🚀 About the Project

**Fofoca Transcriptor** is a personal, modular toolkit built in Python to handle media transcription and text-to-speech synthesis **100% offline**. Powered by state-of-the-art open-source AI models, it gives you complete control over your files, running safely right on your local machine with zero cloud dependencies or external API calls.

---

## 🛠️ Modules & Architecture

The repository is organized into independent, modular subprojects:

1. **`audio-to-text/`**
   * **Engine:** OpenAI Whisper
   * **Features:** Intelligent transcription of audio and video files into precise text, complete with timestamps and zero cloud costs.
2. **`text-to-audio/`**
   * **Engine:** Piper TTS (Offline Fast Neural TTS)
   * **Features:** Converts raw text files into high-quality, natural-sounding audio (`.wav`) locally using ONNX neural voice models (supporting Portuguese and English), ideal for listening on the go or practicing languages.

---

## 📂 Project Structure

```text
fofoca/
├── assets/           # Project visual assets
├── audio-to-text/
│   ├── input/        # Place your source audio/video files here
│   ├── output/       # Generated transcripts (.txt)
│   └── src/          # Transcription scripts (Whisper)
├── text-to-audio/
│   ├── input/        # Text documents (.txt) to be converted into speech
│   ├── models/       # Local ONNX voice models & JSON configs (Piper TTS)
│   │   ├── pt_BR-faber-medium.onnx
│   │   ├── pt_BR-faber-medium.onnx.json
│   │   ├── en_US-lessac-medium.onnx
│   │   └── en_US-lessac-medium.onnx.json
│   ├── output/       # Generated local audio files (.wav)
│   └── src/          # Text-to-speech synthesis scripts (Piper TTS)
├── logo.png          # Project logo
├── pyproject.toml    # Project dependencies and configuration (managed by uv)
└── README.md         # Project documentation
```

---

## 🔧 Getting Started

### Prerequisites

* Python 3.12+
* FFmpeg (for audio/video processing)
* [uv](https://github.com/astral-sh/uv) (fast Python package manager)

### Installation

1. Initialize the Python environment and install dependencies:

   ```bash
   uv sync
   ```

2. (Optional) Download voice models for Piper TTS (if not already present):

   ```bash
   # Portuguese (pt_BR)
   curl -L -o "text-to-audio/models/pt_BR-faber-medium.onnx" "https://huggingface.co/rhasspy/piper-voices/resolve/main/pt/pt_BR/faber/medium/pt_BR-faber-medium.onnx"
   curl -L -o "text-to-audio/models/pt_BR-faber-medium.onnx.json" "https://huggingface.co/rhasspy/piper-voices/resolve/main/pt/pt_BR/faber/medium/pt_BR-faber-medium.onnx.json"

   # English (en_US)
   curl -L -o "text-to-audio/models/en_US-lessac-medium.onnx" "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/lessac/medium/en_US-lessac-medium.onnx"
   curl -L -o "text-to-audio/models/en_US-lessac-medium.onnx.json" "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/lessac/medium/en_US-lessac-medium.onnx.json"
   ```

---

## 📖 Sample Data & Dedication

As an example of our Text-to-Speech pipeline, this repository includes a sample reading of Ecclesiastes 3 (*"For everything there is a season, and a time for every matter under heaven..."*).

> This project is dedicated with all my heart to God, the source of all wisdom and inspiration, whose Word guides every step of this journey.

---

## 🎓 Audio-to-Text Module (Whisper)

Convert spoken content into text with high precision.

### How to Use

1. Place your audio or video files in the `audio-to-text/input/` directory.
2. Run the transcription script:

   ```bash
   uv run python audio-to-text/src/transcriber.py
   ```

The generated text files with timestamps will appear in `audio-to-text/output/`.

---

## 🔊 Text-to-Audio Module (Piper TTS)

Convert written text into natural speech **100% offline** using local neural ONNX models.

### How to Use

1. Add your text files (`.txt`) to the `text-to-audio/input/` directory.
2. Execute the speaker script:

   ```bash
   uv run python text-to-audio/src/speaker.py
   ```

The resulting audio files (`.wav`) will be saved in `text-to-audio/output/`.

### Language & Voice Models

The module automatically maps languages to offline ONNX models:

* **Portuguese (`pt` / `pt_br`)**: `pt_BR-faber-medium.onnx`
* **English (`en` / `en_us`)**: `en_US-lessac-medium.onnx`

---

## 🔐 Privacy & Security

* **100% Local Processing:** All operations happen on your device. No data leaves your computer.
* **No Cloud / No Paywalls:** Built entirely on free, open-source technologies without subscriptions.
* **Unlimited Use:** No file size limits, no usage quotas, no restrictive daily caps.

---

## 👥 Contributing

Contributions are welcome! Whether you want to improve performance, add new features, or help with documentation, your input is valuable. Feel free to open an issue or submit a pull request.

---

## 📄 License

This project is open-source and available under the MIT License.
