import os
from app.core.config import EXECUTION_MODE

def play_music(text: str) -> str:
    if EXECUTION_MODE != "local":
        return "Music playback is only available in local mode."

    music_dir = "C:/Users/Public/Music"

    for file in os.listdir(music_dir):
        if file.endswith(".mp3"):
            os.startfile(os.path.join(music_dir, file))
            return f"Playing {file} 🎵"

    return "No music files found."
