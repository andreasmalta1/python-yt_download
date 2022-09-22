from pytube import YouTube

link = input('Please enter your link: ')
yt = YouTube(link)
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()