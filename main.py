from pytube import YouTube
import os
import ffmpeg

def download_progressive_streams(yt, link):
    link = input('Please enter your link: ')
    yt = YouTube(link)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()


def download_adaptive_stream(yt, link):
    video = yt.streams.filter(adaptive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    os.rename(video, 'video.mp4')

    audio = yt.streams.filter(only_audio=True)[0].download()
    os.rename(audio, 'audio.mp4')

    video_stream = ffmpeg.input('video.mp4')
    audio_stream = ffmpeg.input('audio.mp4')

    ffmpeg.output(audio_stream, video_stream, 'out.mp4', loglevel="quiet").run()
    os.rename('out.mp4', yt.title + '.mp4')
    os.remove('audio.mp4')
    os.remove('video.mp4')


def main():
    link = input('Please enter your link: ')
    yt = YouTube(link)
    download_progressive_streams(yt, link)
    download_adaptive_stream(yt, link)
