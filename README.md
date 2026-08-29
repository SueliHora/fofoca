# 🦭 Fofoca™ Ecosystem

> Um ecossistema local, inteligente e **100% gratuito** para processamento de áudio, vídeo e texto, feito para quem busca produtividade, autonomia e estudos de idiomas sem esbarrar em paywalls ou limites de tamanho.

<p align="center">
  <img src="logo/logo.png" alt="Fofoca Logo" width="300" style="border-radius: 50%;">
</p>

---

## 📂 Arquitetura do Projeto

O repositório é dividido em módulos especializados:

1. **`audio-to-text/`**: Transcrição local de alta precisão usando **OpenAI Whisper** (suporta áudios e vídeos, com detecção automática de idioma e minutagens).
2. **`text-to-audio/`**: Módulo de síntese de voz (Text-to-Speech) para conversão de roteiros em arquivos de áudio.

---

## 🚀 Tecnologias Utilizadas

* **Python 3.10+**
* **OpenAI Whisper**
* **FFmpeg**
* **uv** (Gerenciador de dependências)

---

## 📦 Como Usar o Módulo Audio-to-Text

1. Sincronize o ambiente com o `uv`:

   ```bash
   uv sync
   ```

2. Coloque seus arquivos de áudio ou vídeo na pasta `input/`.
3. Execute o script:

   ```bash
   uv run python audio-to-text/src/transcriber.py
   ```

Os arquivos de texto gerados com timestamps aparecerão na pasta `output/`.

---

## 🎚️ Controle de Qualidade e Velocidade

Você pode ajustar o equilíbrio entre qualidade e velocidade escolhendo entre diferentes modelos do Whisper na variável `MODEL_SIZE` do arquivo `config.py`.

* **Modelos disponíveis (do menor para o maior):**
  * `tiny` (mais rápido, menor precisão)
  * `base` (balanceado)
  * `small` (mais lento, maior precisão)
  * `medium` (ainda mais lento, ainda maior precisão)
  * `large` (o mais lento e mais preciso)
