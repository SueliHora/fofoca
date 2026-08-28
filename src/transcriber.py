import os
import subprocess
import whisper

SUPPORTED_VIDEOS = (".mp4", ".mkv", ".mov", ".avi")
SUPPORTED_AUDIOS = (".mp3", ".wav", ".m4a", ".aac")

def get_input_file(input_dir="input"):
    """Finds the first valid media file inside the input directory."""
    if not os.path.exists(input_dir):
        os.makedirs(input_dir, exist_ok=True)
        return None

    files = [f for f in os.listdir(input_dir) if not f.startswith(".")]
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if ext in SUPPORTED_VIDEOS or ext in SUPPORTED_AUDIOS:
            return os.path.join(input_dir, file)
    return None

def convert_video_to_audio(video_path, output_audio_path):
    """Uses FFmpeg to extract audio from a video file into MP3."""
    print(f"[FFmpeg] Extracting audio from '{video_path}'...")
    cmd = ["ffmpeg", "-y", "-i", video_path, "-vn", output_audio_path]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"[FFmpeg] Audio successfully extracted to: {output_audio_path}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[Error] Failed to convert video with FFmpeg: {e}")
        return False

def transcribe_audio(audio_path, output_dir="output", original_name="transcription"):
    """Loads OpenAI Whisper model and transcribes the local audio file with timestamps."""
    os.makedirs(output_dir, exist_ok=True)
    output_txt_path = os.path.join(output_dir, f"{original_name}.txt")

    try:
        print("[Whisper] Loading the 'base' model into memory...")
        model = whisper.load_model("base")

        print(f"[Whisper] Transcribing '{audio_path}' with timestamps. This might take a few minutes...")
        result = model.transcribe(audio_path, language="pt")

        # Saving with timestamps and clean formatting
        with open(output_txt_path, "w", encoding="utf-8") as f:
            for segment in result["segments"]:
                start_sec = segment["start"]
                minutes = int(start_sec // 60)
                seconds = int(start_sec % 60)
                timestamp_str = f"[{minutes:02d}:{seconds:02d}]"
                
                text = segment["text"].strip()
                f.write(f"{timestamp_str} {text}\n")

        print(f"\n[Success] Fofoca Transcriptor finished with timestamps! 🦭✨")
        print(f"Transcription saved at: {output_txt_path}")

    except Exception as e:
        print(f"[Error] An unexpected error occurred during transcription: {e}")

def main():
    media_path = get_input_file("input")
    
    if not media_path:
        print("[Error] No valid audio or video file found inside the 'input' folder.")
        print("Please place a media file (.mp3, .mp4, etc.) in 'input/' and try again.")
        return

    base_name = os.path.splitext(os.path.basename(media_path))[0]
    ext = os.path.splitext(media_path)[1].lower()

    # If it is a video, extract to MP3 first
    if ext in SUPPORTED_VIDEOS:
        audio_temp_path = os.path.join("input", f"{base_name}_extracted.mp3")
        if convert_video_to_audio(media_path, audio_temp_path):
            transcribe_audio(audio_temp_path, original_name=base_name)
    else:
        # If it's already an audio file (.mp3, .wav, etc.)
        transcribe_audio(media_path, original_name=base_name)

if __name__ == "__main__":
    main()