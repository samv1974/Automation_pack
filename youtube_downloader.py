from pytube import YouTube

def download_video(youtube_url,save_path='.'):
    try:
        yt = YouTube(youtube_url)
        print(f"Title : {yt.title}")
        print(f"Duration:{yt.length//60} minutes")

        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=save_path)

        print(f"Downloaded successfully to '{save_path}'")

    except Exception as e:
        print(f"❌Error:{e}")

# Example usage:
# download_video('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
