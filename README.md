# 🎵 Spotify Playlist Downloader & MP3 Analyzer

This repository contains two Python scripts:

1. **`download_playlists.py`** – Downloads Spotify playlists to MP3 using `spotdl`.
2. **`analyze_mp3s.py`** – Scans the downloaded MP3s, extracts metadata (title, artist, album, duration), estimates BPM (beats per minute), detects the most energetic 20-second segment, and exports everything to an Excel spreadsheet.

---

## 🔧 Prerequisites

- Python 3.8+
- [FFmpeg](https://ffmpeg.org/download.html) installed and available in PATH
- Required Python libraries:
  ```bash
  pip install spotdl mutagen librosa pandas openpyxl numpy
  ```

---

## 📥 1. Download Spotify Playlists

**File:** `download_playlists.py`

Downloads 3 hard-coded Spotify playlists into separate folders (`Playlist_1`, `Playlist_2`, `Playlist_3`) using [spotdl](https://github.com/spotDL/spotify-downloader).

### 🔁 Usage:
```bash
python download_playlists.py
```

Ensure `ffmpeg` is installed and working (`ffmpeg -version` should print version info).

---

## 🧠 2. Analyze MP3 Files

**File:** `analyze_mp3s.py`

Scans all `.mp3` files in the current folder (and subfolders), then creates `mp3_analysis.xlsx` with:
- Title
- Artist
- Album
- Duration (s)
- Estimated BPM
- Best Part (e.g., `95-115` seconds)
- File path

### 🔁 Usage:
```bash
python analyze_mp3s.py
```

> ℹ️ The best part is estimated based on the most energetic 20-second segment in the track using short-time energy.

---

## 📂 Output

- `Playlist_1/`, `Playlist_2/`, `Playlist_3/`: folders with downloaded MP3s
- `mp3_analysis.xlsx`: spreadsheet with metadata and audio analysis

---

## 📌 Notes

- BPM is estimated using `librosa`, so results are approximate.
- Energy-based segment detection works best for music with dynamic contrast.
- The playlist URLs are hard-coded in `download_playlists.py`, but you can easily modify them.

---
