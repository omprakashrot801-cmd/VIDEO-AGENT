import os
import yt_dlp


from pydub import AudioSegment
DOWNLOAD_DIR = 'downloads'
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def download_youtube_audio(url: str) -> str:
    output_path = os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s")

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": output_path,

        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
                "preferredquality": "192",
            }
        ],
        "quiet": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = os.path.splitext(ydl.prepare_filename(info))[0] + ".wav"

        return filename
    

if __name__ == "__main__":
    url = input("https://youtu.be/kTXilT_KbUM?si=mRZS-Tu8kJjg8Ixl ").strip()

    if url:
        audio_file = download_youtube_audio(url)
        print("https://youtu.be/kTXilT_KbUM?si=mRZS-Tu8kJjg8Ixl", audio_file)
    else:
        print("https://youtu.be/kTXilT_KbUM?si=mRZS-Tu8kJjg8Ixl")
