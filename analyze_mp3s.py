import subprocess
import os

PLAYLISTS = {
    "Playlist_1": "https://open.spotify.com/playlist/6RR1UeMYnjZPmz7VpomgI9?si=fc6ccb80e56541c2",
    "Playlist_2": "https://open.spotify.com/playlist/1HQQk9KQlnOuLPN7aXCKfC?si=5db40e0c25734df7",
    "Playlist_3": "https://open.spotify.com/playlist/0yNrYR0E0tGshiHi3nQksW?si=bd2447491ce14979"
}

def download_playlist(name, url):
    folder = os.path.join(os.getcwd(), name)
    os.makedirs(folder, exist_ok=True)
    print(f"Downloading {name} into {folder}...")
    subprocess.run(["spotdl", "download", url, "--output", f"{folder}/"], check=True)

if __name__ == "__main__":
    for name, url in PLAYLISTS.items():
        try:
            download_playlist(name, url)
        except subprocess.CalledProcessError as e:
            print(f"Failed to download {name}: {e}")
