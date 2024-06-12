from pytube import Playlist, YouTube

if __name__ == "__main__":
    playlist_url = input("Enter the link of the playlist: ")
    playlist = Playlist(playlist_url) 
    for url in playlist.video_urls:
        video = YouTube(url)
        audio_stream = video.streams.get_audio_only()
        audio_stream.download()
        print("✅ 😎 🎧")
