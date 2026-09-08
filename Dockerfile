# ==============================================================================
# Fofoca™ Transcriptor - Dockerfile
# Optimized multi-stage/layer-cached build using Astral uv and Debian Bookworm
# Includes system binaries for FFmpeg (Whisper ASR) and espeak-ng (Piper TTS)
# ==============================================================================

FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS base

# Install essential system dependencies:
# - ffmpeg: required by OpenAI Whisper for audio extraction and resampling
# - espeak-ng: required by Piper TTS for grapheme-to-phoneme phonemization
# - ca-certificates & curl: SSL certificates and health check probes
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    espeak-ng \
    ca-certificates \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set container working directory
WORKDIR /app

# Configure uv and Python runtime environment
ENV PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    GRADIO_SERVER_NAME="0.0.0.0" \
    GRADIO_SERVER_PORT="7860"

# Install dependencies in a separate layer for maximum Docker build caching
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

# Copy application code into container
COPY . /app

# Sync and install the project itself into virtual environment
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

# Ensure virtual environment executables take precedence in PATH
ENV PATH="/app/.venv/bin:$PATH"

# Expose Gradio Web UI default port
EXPOSE 7860

# Container healthcheck probe against Gradio HTTP endpoint
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
    CMD curl -f http://localhost:7860/ || exit 1

# Default command to start Fofoca Web UI
CMD ["python", "main.py"]
