from pytube import YouTube

url = "https://www.youtube.com/watch?v=9bZkp7q19f0"

yt = YouTube(url)

print(yt.length)