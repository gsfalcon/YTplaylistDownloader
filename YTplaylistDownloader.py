import os
import math
from pytube import Playlist
from yt_dlp import YoutubeDL
from tqdm import tqdm

# Create downloads folder
DOWNLOAD_DIR = "DOWNLOADS"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# User input
playlist_url = input("📎 Paste the YouTube playlist link here: ")

# Get playlist info
playlist = Playlist(playlist_url)
video_urls = playlist.video_urls
total_videos = len(video_urls)

# Estimate total time
seconds_per_video = 11.3  # 7.9s download + 3.4s processing
total_seconds = total_videos * seconds_per_video
estimated_minutes = math.ceil(total_seconds / 60)

print(f"\n🎶 Playlist detected: {playlist.title}")
print(f"📁 Total videos: {total_videos}")
print(f"⏱️ Estimated total time: ~{estimated_minutes} minute(s)")
print("🚀 Starting download...\n")

# Progress bar
progress_bar = tqdm(total=total_videos, desc="🔽 Progress", unit="video")

# YT-DLP options
ydl_opts = {
    'format': 'bestvideo+bestaudio[ext=m4a]/best[ext=mp4]',
    'merge_output_format': 'mp4',
    'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s'),
    'quiet': True,
    'no_warnings': True,
}

# Start downloading
with YoutubeDL(ydl_opts) as ydl:
    for url in video_urls:
        try:
            ydl.download([url])
        except Exception as e:
            print(f"❌ Error downloading {url}: {e}")
        progress_bar.update(1)

progress_bar.close()
print("\n✅ All videos have been processed.")
