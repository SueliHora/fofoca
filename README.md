<div align="center">
  <img src="./logo.png" alt="Fofoca Transcriptor Logo" width="200">
  <h1>🦭 Fofoca Transcriptor</h1>
  <p><b>A local, free, and smart ecosystem for audio, video, and text processing.</b></p>
  <p>Designed for productivity, privacy, autonomy, and language studies without paywalls or size limits.</p>
</div>

---

## 🚀 About the Project

**Fofoca Transcriptor** is a personal, modular toolkit built in Python to handle media transcription and text-to-speech synthesis entirely offline. Powered by state-of-the-art open-source AI models, it gives you complete control over your files, running safely right on your local machine.

---

## 🛠️ Modules & Architecture

The repository is organized into independent, modular subprojects:

1. **`audio-to-text/`**
   * **Engine:** OpenAI Whisper
   * **Features:** Intelligent transcription of audio and video files into precise text, complete with timestamps and zero cloud costs.
2. **`text-to-audio/`**
   * **Engine:** gTTS (Google Text-to-Speech)
   * **Features:** Converts raw text files into natural-sounding audio (.mp3), ideal for listening on the go or practicing languages.

---

## 📂 Project Structure

```text
fofoca/
├── assets/           # Project visual assets
├── audio-to-text/
│   ├── input/        # Place your source audio/video files here
│   ├── output/       # Generated transcripts
│   └── src/          # Transcription scripts
├── text-to-audio/
│   ├── input/        # Text documents (.txt) to be spoken
│   ├── output/       # Generated audio files (.mp3)
│   └── src/          # Text-to-speech scripts
├── logo.png          # Project logo
├── pyproject.toml    # Project dependencies and configuration (managed by uv)
└── README.md         # Project documentation
```

---

## 🔧 Getting Started

### Prerequisites

* Python 3.10+
* FFmpeg (for audio/video processing)
* uv (dependency manager)

### Installation

1. Initialize the Python environment and install dependencies:

   ```bash
   uv sync
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

### Quality Settings

Control the trade-off between speed and accuracy by adjusting the `MODEL_SIZE` variable in `config.py`:

* **`tiny`**: Fastest, lowest accuracy
* **`base`**: Balanced
* **`small`**: Slower, higher accuracy
* **`medium`**: Slower still, higher accuracy
* **`large`**: Slowest, highest accuracy

---

## 🔊 Text-to-Audio Module (gTTS)

Convert written text into natural speech.

### How to Use

1. Add your text files (`.txt`) to the `text-to-audio/input/` directory.
2. Execute the speaker script:

   ```bash
   uv run python text-to-audio/src/speaker.py
   ```

The resulting audio files (`.mp3`) will be saved in `text-to-audio/output/`.

---

## 🔐 Privacy & Security

* **100% Local Processing:** All operations happen on your device. No data leaves your computer.
* **No Paywalls:** Built entirely on free, open-source technologies.
* **Unlimited Use:** No file size limits, no usage quotas, no hidden costs.

---

## 👥 Contributing

Contributions are welcome! Whether you want to improve performance, add new features, or help with documentation, your input is valuable. Feel free to open an issue or submit a pull request.

---

## 📄 License

This project is open-source and available under the MIT License.
