import os
import yt_dlp
import shutil

def download_playlist(playlist_url, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    ydl_opts = {
        'outtmpl': os.path.join(output_dir, '%(title).200s.%(ext)s'),
        'format': 'bv*[height<=720]+ba/b[height<=720]',  # up to 720p
        'merge_output_format': 'mp4'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

def zip_directory(source_dir, zip_name):
    shutil.make_archive(zip_name, 'zip', source_dir)
    print(f"✅ Zipped to {zip_name}.zip")

if __name__ == "__main__":
    playlist_url = "https://youtube.com/playlist?list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0"
    output_dir = r"C:\Users\Nirav\OneDrive\Desktop\course\videos"
    zip_name = r"C:\Users\Nirav\OneDrive\Desktop\course\CampusX_Playlist"

    print("🎬 Downloading playlist...")
    download_playlist(playlist_url, output_dir)

    print("📦 Zipping downloaded videos...")
    zip_directory(output_dir, zip_name)

    print(f"✅ Done! Zipped file at: {zip_name}.zip")

 