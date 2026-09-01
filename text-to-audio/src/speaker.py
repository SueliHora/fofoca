import sys
import wave
from pathlib import Path

from piper.voice import PiperVoice

# Ensure UTF-8 output encoding for terminals (especially Windows cp1252)
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Base paths calculation for robust execution from any working directory
SCRIPT_DIR = Path(__file__).resolve().parent
MODULE_DIR = SCRIPT_DIR.parent
PROJECT_ROOT = MODULE_DIR.parent

DEFAULT_INPUT_DIR = MODULE_DIR / "input"
DEFAULT_OUTPUT_DIR = MODULE_DIR / "output"
DEFAULT_MODELS_DIR = MODULE_DIR / "models"

MODEL_MAP = {
    "pt": "pt_BR-faber-medium.onnx",
    "pt_br": "pt_BR-faber-medium.onnx",
    "en": "en_US-lessac-medium.onnx",
    "en_us": "en_US-lessac-medium.onnx",
}


def get_model_path(language: str = "pt", models_dir: Path | None = None) -> Path:
    """Resolves the ONNX model file path for the requested language."""
    models_dir = Path(models_dir) if models_dir else DEFAULT_MODELS_DIR
    lang_key = language.strip().lower().replace("-", "_")

    model_filename = MODEL_MAP.get(lang_key)
    if not model_filename:
        supported = ", ".join(MODEL_MAP.keys())
        raise ValueError(
            f"Unsupported language '{language}'. Supported options: {supported}"
        )

    model_path = models_dir / model_filename
    if not model_path.exists():
        raise FileNotFoundError(
            f"Piper model not found at '{model_path}'. "
            f"Please download '{model_filename}' into '{models_dir}'."
        )

    return model_path


def synthesize_text_to_wav(
    text: str,
    output_wav_path: str | Path,
    language: str = "pt",
    models_dir: Path | None = None,
) -> Path:
    """
    Synthesizes speech from raw text using Piper TTS (100% offline) and saves as a .wav file.

    :param text: Text string to synthesize.
    :param output_wav_path: Target path for the output .wav file.
    :param language: Language code ('pt', 'pt_br', 'en', 'en_us').
    :param models_dir: Directory containing Piper ONNX models.
    :return: Path to the generated .wav file.
    """
    output_wav = Path(output_wav_path)
    output_wav.parent.mkdir(parents=True, exist_ok=True)

    model_path = get_model_path(language=language, models_dir=models_dir)
    config_path = model_path.with_suffix(".onnx.json")

    # Load offline Piper voice model
    voice = PiperVoice.load(
        model_path=str(model_path),
        config_path=str(config_path) if config_path.exists() else None,
    )

    with wave.open(str(output_wav), "wb") as wav_file:
        voice.synthesize_wav(text, wav_file)

    return output_wav


def convert_text_to_speech(
    txt_path: str | Path,
    output_dir: str | Path | None = None,
    language: str = "pt",
    models_dir: Path | None = None,
) -> Path | None:
    """Reads a text file and converts it into a local WAV audio file using Piper TTS."""
    txt_file = Path(txt_path)
    target_output_dir = Path(output_dir) if output_dir else DEFAULT_OUTPUT_DIR
    target_output_dir.mkdir(parents=True, exist_ok=True)

    output_wav_path = target_output_dir / f"{txt_file.stem}.wav"

    try:
        print(f"[Piper TTS] Reading text from '{txt_file}'...")
        with open(txt_file, "r", encoding="utf-8") as f:
            text_content = f.read().strip()

        if not text_content:
            print(f"[Warning] The file '{txt_file}' is empty. Skipping.")
            return None

        print(f"[Piper TTS] Generating audio (Language: {language}, Offline)...")
        synthesize_text_to_wav(
            text=text_content,
            output_wav_path=output_wav_path,
            language=language,
            models_dir=models_dir,
        )

        print("\n[Success] Audio generated successfully! 🦭✨")
        print(f"Saved at: {output_wav_path}\n" + "-" * 50)
        return output_wav_path

    except Exception as e:
        print(f"[Error] Failed to convert text to speech: {e}")
        return None


def get_all_text_files(input_dir: str | Path | None = None) -> list[Path]:
    """Finds all valid .txt files inside the input directory."""
    target_input_dir = Path(input_dir) if input_dir else DEFAULT_INPUT_DIR
    if not target_input_dir.exists():
        target_input_dir.mkdir(parents=True, exist_ok=True)
        return []

    return [
        f
        for f in target_input_dir.iterdir()
        if f.is_file() and not f.name.startswith(".") and f.suffix.lower() == ".txt"
    ]


def main():
    txt_paths = get_all_text_files(DEFAULT_INPUT_DIR)

    if not txt_paths:
        print(f"[Error] No .txt files found inside '{DEFAULT_INPUT_DIR}'.")
        print("Please place a text file there and try again.")
        return

    print(f"[Fofoca Speaker] Found {len(txt_paths)} file(s) to convert. Let's go! 🦭🚀\n")

    for txt_path in txt_paths:
        convert_text_to_speech(txt_path, output_dir=DEFAULT_OUTPUT_DIR, language="pt")

    print("\n[Fofoca Speaker] All texts converted to audio successfully! 🎉")


if __name__ == "__main__":
    main()