import os
import subprocess

def download_youtube_as_mp3(youtube_url, save_folder):
    try:
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
        command = [
            "yt-dlp",
            "--extract-audio",
            "--audio-format", "mp3",
            "--output", f"{save_folder}/%(title)s.%(ext)s",
            youtube_url
        ]
        subprocess.run(command, check=True)
        print("Download and conversion completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    save_folder = "songs"
    youtube_url = input("Enter the YouTube video URL: ")
    download_youtube_as_mp3(youtube_url, save_folder)