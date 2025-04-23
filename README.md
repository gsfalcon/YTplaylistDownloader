# 🎥 YTplaylistDownloader

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![yt-dlp](https://img.shields.io/badge/Powered_by-yt--dlp-yellow)](https://github.com/yt-dlp/yt-dlp)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

> ⚡ Download entire YouTube playlists with automatic audio+video merging, saving to `.mp4` in seconds!

---

## 🚀 Features

| Feature             | Description                                                                  |
|--------------------|------------------------------------------------------------------------------|
| 📥 Bulk Download    | Downloads all videos from a given playlist link                              |
| 🎞️ MP4 Format       | Combines best video + best audio and saves as `.mp4`                         |
| ⏱️ Time Estimation  | Calculates estimated time for full download + conversion                     |
| 📁 Organized Output | Automatically saves all files into a `DOWNLOADS/` folder                     |
| 🔁 Auto-Retry       | Retries failed downloads and skips unavailable videos                        |

---

## 🛠️ Requirements

Make sure you have Python 3.11+ installed, then install the dependencies:

```bash
pip install yt-dlp tqdm pytube
```

---

## 📦 Usage

Run the script using Python:

```bash
python YTplaylistDownloader.py
```

You will be prompted to paste a YouTube playlist URL. The script will then:

1. Detect playlist title and number of videos
2. Estimate total download & processing time
3. Download and merge audio/video for each item
4. Save each result as an `.mp4` file inside the `DOWNLOADS/` folder

---

## 📸 Screenshot

```
🎶 Playlist detected: Horizon Forbidden West
📁 Total videos: 7
🕒 Estimated time: 00h 04m 45s
🚀 Starting download...
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 💡 Tip

Using a wired connection and avoiding background downloads will help achieve better speeds.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 🔗 Useful Links

- [yt-dlp Documentation](https://github.com/yt-dlp/yt-dlp)
- [Python Downloads](https://www.python.org/downloads/)
- [FFmpeg Installation Guide](https://ffmpeg.org/download.html)
