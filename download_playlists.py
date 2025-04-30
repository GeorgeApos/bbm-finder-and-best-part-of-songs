import os
import librosa
import numpy as np
import pandas as pd
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

def analyze_mp3(file_path):
    try:
        audio = MP3(file_path, ID3=EasyID3)
        metadata = {
            'Title': audio.get('title', ['Unknown'])[0],
            'Artist': audio.get('artist', ['Unknown'])[0],
            'Album': audio.get('album', ['Unknown'])[0]
        }
        duration = audio.info.length
        metadata['Duration (s)'] = round(duration, 2)

        y, sr = librosa.load(file_path, duration=duration)

        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
        if isinstance(tempo, (list, tuple, np.ndarray)):
            tempo = float(tempo[0])
        metadata['Estimated BPM'] = round(tempo, 2)

        frame_length = sr * 20
        step = sr * 5
        energies = [
            (i, sum(abs(y[i:i+frame_length])))
            for i in range(0, len(y) - frame_length, step)
        ]
        if energies:
            best_start, _ = max(energies, key=lambda x: x[1])
            best_part_start = best_start / sr
            best_part_end = (best_start + frame_length) / sr
            metadata['Best Part (s)'] = f"{int(best_part_start)}-{int(best_part_end)}"
        else:
            metadata['Best Part (s)'] = "N/A"

        return metadata
    except Exception as e:
        print(f"Error analyzing {file_path}: {e}")
        return None

def analyze_folder(base_folder):
    results = []
    for root, _, files in os.walk(base_folder):
        for file in files:
            if file.endswith('.mp3'):
                path = os.path.join(root, file)
                print(f"Analyzing: {path}")
                info = analyze_mp3(path)
                if info:
                    info['File'] = path
                    results.append(info)

    df = pd.DataFrame(results)
    df.to_excel("mp3_analysis.xlsx", index=False)
    print("\n✅ Analysis complete. Results saved to mp3_analysis.xlsx")

if __name__ == "__main__":
    analyze_folder(os.getcwd())
