import os
import whisper

SUPPORTED_VIDEOS = (".mp4", ".mkv", ".mov", ".avi")
SUPPORTED_AUDIOS = (".mp3", ".wav", ".m4a", ".aac")

def get_all_input_files(input_dir="input"):
    """Finds all valid media files inside the input directory."""
    if not os.path.exists(input_dir):
        os.makedirs(input_dir, exist_ok=True)
        return []

    files = [f for f in os.listdir(input_dir) if not f.startswith(".")]
    valid_files = []
    
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if ext in SUPPORTED_VIDEOS or ext in SUPPORTED_AUDIOS:
            valid_files.append(os.path.join(input_dir, file))
            
    return valid_files

def transcribe_media(media_path, output_dir="output"):
    """Loads OpenAI Whisper model and transcribes audio/video directly with timestamps."""
    os.makedirs(output_dir, exist_ok=True)
    base_name = os.path.splitext(os.path.basename(media_path))[0]
    output_txt_path = os.path.join(output_dir, f"{base_name}.txt")

    try:
        print("[Whisper] Loading the 'base' model into memory...")
        model = whisper.load_model("base")

        print(f"[Whisper] Transcribing '{media_path}' (auto-detecting language) with timestamps...")
        result = model.transcribe(media_path)

        # Saving with timestamps and clean formatting
        with open(output_txt_path, "w", encoding="utf-8") as f:
            for segment in result["segments"]:
                start_sec = segment["start"]
                minutes = int(start_sec // 60)
                seconds = int(start_sec % 60)
                timestamp_str = f"[{minutes:02d}:{seconds:02d}]"
                
                text = segment["text"].strip()
                f.write(f"{timestamp_str} {text}\n")

        print(f"\n[Success] Transcription finished with timestamps! 🦭✨")
        print(f"Saved at: {output_txt_path}\n" + "-"*50)

    except Exception as e:
        print(f"[Error] An unexpected error occurred during transcription: {e}")

def main():
    media_paths = get_all_input_files("input")
    
    if not media_paths:
        print("[Error] No valid audio or video files found inside the 'input' folder.")
        return

    print(f"[Fofoca] Found {len(media_paths)} file(s) to process. Let's go! 🦭🚀\n")

    for media_path in media_paths:
        transcribe_media(media_path)

    print("\n[Fofoca] All files processed successfully! 🎉")

if __name__ == "__main__":
    main()