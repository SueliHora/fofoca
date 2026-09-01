"""
Fofoca™ Transcriptor - Main Entry Point
Author: Sueli da Hora Moreira
"""
import gradio as gr

from app import CUSTOM_CSS, demo


def main():
    print("🦭 Iniciando Fofoca™ Transcriptor Web UI...")
    print("Acesse no navegador: http://127.0.0.1:7860")
    demo.launch(
        theme=gr.themes.Soft(primary_hue="indigo"),
        css=CUSTOM_CSS,
        server_name="127.0.0.1",
        server_port=7860,
    )

if __name__ == "__main__":
    main()