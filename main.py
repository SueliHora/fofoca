"""
Fofoca™ Transcriptor - Main Entry Point
Author: Sueli da Hora Moreira
"""

import os

import gradio as gr

from app import CUSTOM_CSS, demo


def main():
    server_name = os.environ.get("GRADIO_SERVER_NAME", "0.0.0.0")
    server_port = int(os.environ.get("GRADIO_SERVER_PORT", os.environ.get("PORT", "7860")))

    print("🦭 Iniciando Fofoca™ Transcriptor Web UI...")
    display_host = "127.0.0.1" if server_name == "0.0.0.0" else server_name
    print(f"Acesse no navegador: http://{display_host}:{server_port}")

    demo.launch(
        theme=gr.themes.Soft(primary_hue="indigo"),
        css=CUSTOM_CSS,
        server_name=server_name,
        server_port=server_port,
    )


if __name__ == "__main__":
    main()
