import os
import sys
from datetime import datetime
from pathlib import Path

import gradio as gr
import whisper

# Ensure UTF-8 output encoding for terminals (especially Windows cp1252)
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Ensure modules in text-to-audio/src are accessible
ROOT_DIR = Path(__file__).resolve().parent
TEXT_TO_AUDIO_DIR = ROOT_DIR / "text-to-audio"
AUDIO_TO_TEXT_DIR = ROOT_DIR / "audio-to-text"

sys.path.insert(0, str(TEXT_TO_AUDIO_DIR / "src"))
from speaker import DEFAULT_MODELS_DIR, synthesize_text_to_wav
from speaker import DEFAULT_OUTPUT_DIR as TTS_OUTPUT_DIR

WHISPER_OUTPUT_DIR = AUDIO_TO_TEXT_DIR / "output"
WHISPER_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
TTS_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Cache for loaded Whisper models to avoid re-loading on each request
_whisper_cache = {}


def get_whisper_model(model_name: str = "base"):
    """Loads and caches the Whisper model in memory."""
    if model_name not in _whisper_cache:
        _whisper_cache[model_name] = whisper.load_model(model_name)
    return _whisper_cache[model_name]


def process_audio_to_text(
    file_path_str: str | None,
    model_size: str = "base",
    include_timestamps: bool = True,
) -> tuple[str, str | None, str]:
    """
    Transcribes uploaded audio or video using local OpenAI Whisper.
    """
    if not file_path_str:
        return "", None, "⚠️ **Por favor, selecione ou envie um arquivo de áudio/vídeo válido.**"

    file_path = Path(file_path_str)
    if not file_path.exists():
        return "", None, "❌ **Arquivo não encontrado no sistema.**"

    base_name = file_path.stem
    timestamp_tag = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_txt_path = WHISPER_OUTPUT_DIR / f"{base_name}_{timestamp_tag}.txt"

    try:
        model = get_whisper_model(model_size)
        result = model.transcribe(str(file_path))

        lines = []
        if include_timestamps and "segments" in result and result["segments"]:
            for segment in result["segments"]:
                start_sec = segment["start"]
                minutes = int(start_sec // 60)
                seconds = int(start_sec % 60)
                timestamp_str = f"[{minutes:02d}:{seconds:02d}]"
                text = segment["text"].strip()
                lines.append(f"{timestamp_str} {text}")
        else:
            lines.append(result.get("text", "").strip())

        transcription_text = "\n".join(lines)

        with open(output_txt_path, "w", encoding="utf-8") as f:
            f.write(transcription_text)

        detected_lang = result.get("language", "auto")
        status_msg = (
            f"✅ **Transcrição concluída com sucesso!** 🦭✨\n\n"
            f"- **Idioma detectado:** `{detected_lang}`\n"
            f"- **Modelo utilizado:** `Whisper ({model_size})`\n"
            f"- **Arquivo salvo em:** `{output_txt_path.relative_to(ROOT_DIR)}`"
        )
        return transcription_text, str(output_txt_path), status_msg

    except Exception as e:
        error_msg = f"❌ **Erro durante a transcrição:** `{e!s}`"
        return "", None, error_msg


def process_text_to_audio(
    text: str,
    language_code: str = "pt",
) -> tuple[str | None, str | None, str]:
    """
    Synthesizes speech from raw text using local Piper TTS (.wav output).
    """
    clean_text = text.strip() if text else ""
    if not clean_text:
        return None, None, "⚠️ **Por favor, digite ou cole um texto para ser sintetizado.**"

    timestamp_tag = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = f"fofoca_audio_{timestamp_tag}.wav"
    output_wav_path = TTS_OUTPUT_DIR / safe_name

    try:
        synthesize_text_to_wav(
            text=clean_text,
            output_wav_path=output_wav_path,
            language=language_code,
            models_dir=DEFAULT_MODELS_DIR,
        )

        model_name = "pt_BR-faber-medium" if language_code == "pt" else "en_US-lessac-medium"
        status_msg = (
            f"✅ **Áudio gerado com sucesso!** 🦭🔊\n\n"
            f"- **Modelo de Voz:** `{model_name}`\n"
            f"- **Processamento:** `100% Offline (Piper TTS)`\n"
            f"- **Arquivo salvo em:** `{output_wav_path.relative_to(ROOT_DIR)}`"
        )
        return str(output_wav_path), str(output_wav_path), status_msg

    except Exception as e:
        error_msg = f"❌ **Erro na síntese de áudio:** `{e!s}`"
        return None, None, error_msg


# Custom CSS for a modern, sleek and polished look
CUSTOM_CSS = """
.main-container {
    max-width: 1100px;
    margin: 0 auto;
    font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
}
.header-badge {
    display: inline-block;
    padding: 4px 14px;
    background: linear-gradient(135deg, #0284c7, #4f46e5);
    color: white !important;
    border-radius: 9999px;
    font-size: 0.8rem;
    font-weight: 700;
    margin-bottom: 8px;
    letter-spacing: 0.05em;
    text-transform: uppercase;
}
.app-title {
    font-size: 2.2rem !important;
    font-weight: 800 !important;
    margin-top: 4px !important;
    margin-bottom: 4px !important;
}
.app-subtitle {
    color: #64748b !important;
    font-size: 1.05rem !important;
    margin-bottom: 16px !important;
}
"""

def create_app() -> gr.Blocks:
    with gr.Blocks(title="Fofoca Transcriptor", analytics_enabled=False) as demo:
        with gr.Column(elem_classes=["main-container"]):
            with gr.Row():
                with gr.Column(scale=1):
                    gr.HTML("""
                    <div style="text-align: center; padding: 12px 0 18px 0;">
                        <span class="header-badge">100% Offline • Local & Privado</span>
                        <h1 class="app-title">🦭 Fofoca Transcriptor</h1>
                        <p class="app-subtitle">Ecossistema autônomo para transcrição de mídia e síntese de voz neural</p>
                    </div>
                    """)

            with gr.Tabs():
                # Tab 1: Audio-to-Text (Whisper)
                with gr.TabItem("🎙️ Audio-to-Text (Whisper)", id="tab_transcribe"):
                    gr.Markdown(
                        "Converta arquivos de áudio ou vídeo em texto com alta precisão e marcações de tempo usando o modelo OpenAI Whisper local."
                    )
                    with gr.Row():
                        with gr.Column(scale=5):
                            input_media = gr.File(
                                label="Selecione o arquivo de Áudio / Vídeo",
                                file_types=["audio", "video"],
                                type="filepath",
                            )
                            with gr.Row():
                                whisper_model_choice = gr.Dropdown(
                                    choices=["tiny", "base", "small", "medium", "large"],
                                    value="base",
                                    label="Tamanho do Modelo Whisper",
                                    info="Modelos maiores oferecem maior precisão; menores são mais rápidos.",
                                )
                                timestamps_checkbox = gr.Checkbox(
                                    value=True,
                                    label="Incluir Timestamps [MM:SS]",
                                    info="Adiciona o tempo no início de cada trecho.",
                                )

                            btn_transcribe = gr.Button(
                                "Iniciar Transcrição 🚀",
                                variant="primary",
                                size="lg",
                            )

                        with gr.Column(scale=6):
                            output_text = gr.Textbox(
                                label="Texto Transcrito",
                                placeholder="A transcrição aparecerá aqui...",
                                lines=12,
                                buttons=["copy"],
                            )
                            download_txt = gr.File(label="📄 Baixar Arquivo de Transcrição (.txt)")
                            status_transcribe = gr.Markdown()

                    btn_transcribe.click(
                        fn=process_audio_to_text,
                        inputs=[input_media, whisper_model_choice, timestamps_checkbox],
                        outputs=[output_text, download_txt, status_transcribe],
                    )

                # Tab 2: Text-to-Audio (Piper TTS)
                with gr.TabItem("🔊 Text-to-Audio (Piper TTS)", id="tab_speak"):
                    gr.Markdown(
                        "Transforme textos em fala com voz natural utilizando o Piper TTS 100% offline e modelos ONNX locais."
                    )
                    with gr.Row():
                        with gr.Column(scale=5):
                            input_text = gr.Textbox(
                                label="Texto a ser falado",
                                placeholder="Digite ou cole aqui o texto que deseja sintetizar em áudio...",
                                lines=8,
                            )
                            voice_choice = gr.Radio(
                                choices=[
                                    ("🇧🇷 Português (pt_BR - Faber)", "pt"),
                                    ("🇺🇸 English (en_US - Lessac)", "en"),
                                ],
                                value="pt",
                                label="Voz & Idioma",
                                info="Modelos neurais locais carregados de text-to-audio/models/",
                            )
                            btn_speak = gr.Button(
                                "Gerar Áudio Local 🔊",
                                variant="primary",
                                size="lg",
                            )

                        with gr.Column(scale=6):
                            output_audio = gr.Audio(
                                label="Player de Áudio",
                                type="filepath",
                                interactive=False,
                            )
                            download_wav = gr.File(label="💾 Baixar Áudio (.wav)")
                            status_speak = gr.Markdown()

                    btn_speak.click(
                        fn=process_text_to_audio,
                        inputs=[input_text, voice_choice],
                        outputs=[output_audio, download_wav, status_speak],
                    )

            gr.HTML("""
            <div style="text-align: center; margin-top: 30px; font-size: 0.85rem; color: #94a3b8;">
                🦭 <b>Fofoca Transcriptor</b> • Criado por Sueli da Hora Moreira • Sem paywalls, sem limites de tamanho, 100% privado.
            </div>
            """)

    return demo


demo = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    demo.launch(
        theme=gr.themes.Soft(primary_hue="indigo"),
        css=CUSTOM_CSS,
        server_name="0.0.0.0",
        server_port=port,
    )
