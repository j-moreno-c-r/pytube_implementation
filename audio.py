from pytube import YouTube
if __name__ == "__main__":
    link = input("Enter the link of the audio: ")
    video = YouTube(link)
    audio_stream = video.streams.get_audio_only()
    audio_stream.download()
