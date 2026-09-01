import sys
from pathlib import Path
import pytest
import gradio as gr

# Ensure root directory and subsystem paths are in sys.path
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

TEXT_TO_AUDIO_SRC = ROOT_DIR / "text-to-audio" / "src"
AUDIO_TO_TEXT_SRC = ROOT_DIR / "audio-to-text" / "src"

if str(TEXT_TO_AUDIO_SRC) not in sys.path:
    sys.path.insert(0, str(TEXT_TO_AUDIO_SRC))
if str(AUDIO_TO_TEXT_SRC) not in sys.path:
    sys.path.insert(0, str(AUDIO_TO_TEXT_SRC))


def test_essential_directories_exist():
    """Validates that all essential workspace directories exist."""
    required_directories = [
        ROOT_DIR / "docs",
        ROOT_DIR / "assets",
        ROOT_DIR / "audio-to-text",
        ROOT_DIR / "audio-to-text" / "src",
        ROOT_DIR / "audio-to-text" / "input",
        ROOT_DIR / "audio-to-text" / "output",
        ROOT_DIR / "text-to-audio",
        ROOT_DIR / "text-to-audio" / "src",
        ROOT_DIR / "text-to-audio" / "models",
        ROOT_DIR / "text-to-audio" / "input",
        ROOT_DIR / "text-to-audio" / "output",
    ]
    for directory in required_directories:
        assert directory.exists(), f"Expected directory does not exist: {directory}"
        assert directory.is_dir(), f"Expected path is not a directory: {directory}"


def test_essential_documentation_exists():
    """Validates that documentation and configuration template files exist."""
    required_files = [
        ROOT_DIR / "README.md",
        ROOT_DIR / "README_pt.md",
        ROOT_DIR / "docs" / "PRD.md",
        ROOT_DIR / "docs" / "ARCHITECTURE.md",
        ROOT_DIR / ".env.example",
        ROOT_DIR / "pyproject.toml",
    ]
    for file_path in required_files:
        assert file_path.exists(), f"Expected file does not exist: {file_path}"
        assert file_path.is_file(), f"Expected path is not a file: {file_path}"


def test_module_imports():
    """Validates that core application and subsystem modules can be imported."""
    import app
    import speaker
    import transcriber

    assert hasattr(app, "create_app")
    assert hasattr(speaker, "synthesize_text_to_wav")
    assert hasattr(transcriber, "transcribe_media")


def test_speaker_model_mapping():
    """Validates that the Piper TTS speaker module defines expected language keys."""
    import speaker

    assert "pt" in speaker.MODEL_MAP
    assert "en" in speaker.MODEL_MAP
    assert speaker.MODEL_MAP["pt"].endswith(".onnx")
    assert speaker.MODEL_MAP["en"].endswith(".onnx")


def test_transcriber_supported_extensions():
    """Validates that the Whisper transcriber module defines media extensions."""
    import transcriber

    assert ".mp3" in transcriber.SUPPORTED_AUDIOS
    assert ".wav" in transcriber.SUPPORTED_AUDIOS
    assert ".mp4" in transcriber.SUPPORTED_VIDEOS
    assert ".mkv" in transcriber.SUPPORTED_VIDEOS


def test_gradio_app_structure():
    """Validates that the Gradio app instantiates properly as a gr.Blocks object."""
    import app

    demo = app.create_app()
    assert isinstance(demo, gr.Blocks)
