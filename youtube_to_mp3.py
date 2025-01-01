import os 
from pytube import YouTube
from pydub import AudioSegment
def download_youtube_as_mp3(youtube_url, save_folder):
    try:
        if not os.path.exists(save_folder):
            os.makedirs(save_folder)
        yt = YouTube(youtube_url)
        print(f"Downloading: {yt.title}")
        audio_stream = yt.streams.filter(only_audio=True).first()
        download_path = audio_stream.download(output_path=save_folder)
        base, ext = os.path.splitext(download_path)
        mp3_path = base + ".mp3"
        AudioSegment.from_file(download_path).export(mp3_path, format="mp3")
        os.remove(download_path)
        print(f"Saved MP3: {mp3_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    save_folder = "songs"
    youtube_url = input("Enter the YouTube video URL: ")
    download_youtube_as_mp3(youtube_url, save_folder)
    