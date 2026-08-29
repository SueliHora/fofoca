import os
from gtts import gTTS

def get_all_text_files(input_dir="text-to-audio/input"):
    """Finds all valid text files inside the input directory."""
    if not os.path.exists(input_dir):
        os.makedirs(input_dir, exist_ok=True)
        return []

    files = [f for f in os.listdir(input_dir) if not f.startswith(".")]
    return [os.path.join(input_dir, f) for f in files if f.endswith(".txt")]

def convert_text_to_speech(txt_path, output_dir="text-to-audio/output"):
    """Reads a text file and converts it into an MP3 audio file using gTTS."""
    os.makedirs(output_dir, exist_ok=True)
    base_name = os.path.splitext(os.path.basename(txt_path))[0]
    output_mp3_path = os.path.join(output_dir, f"{base_name}.mp3")

    try:
        print(f"[gTTS] Reading text from '{txt_path}'...")
        with open(txt_path, "r", encoding="utf-8") as f:
            text_content = f.read().strip()

        if not text_content:
            print(f"[Warning] The file '{txt_path}' is empty. Skipping.")
            return

        print(f"[gTTS] Converting text to speech (Language: auto/pt)...")
        # lang="pt" pode ser ajustado ou detectado, por padrão deixamos em português ou inglês
        tts = gTTS(text=text_content, lang="pt", slow=False)
        
        tts.save(output_mp3_path)
        print(f"\n[Success] Audio generated successfully! 🦭✨")
        print(f"Saved at: {output_mp3_path}\n" + "-"*50)

    except Exception as e:
        print(f"[Error] Failed to convert text to speech: {e}")

def main():
    txt_paths = get_all_text_files("text-to-audio/input")
    
    if not txt_paths:
        print("[Error] No .txt files found inside 'text-to-audio/input/'.")
        print("Please place a text file there and try again.")
        return

    print(f"[Fofoca Speaker] Found {len(txt_paths)} file(s) to convert. Let's go! 🦭🚀\n")

    for txt_path in txt_paths:
        convert_text_to_speech(txt_path)

    print("\n[Fofoca Speaker] All texts converted to audio successfully! 🎉")

if __name__ == "__main__":
    main()