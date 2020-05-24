from pytube import YouTube

print("*************************************************")
print("                   YouPy 1.0                  ")
print("*************************************************\n\n")

print('''
This sofwtare enables the user to download videos from youtube
given the link of the video provided by the user.
It is an open source software made on top of pytube library.
The software is under continous developement so, make sure to download
the latest version for bug free experience.
The link to the repo is provided downbelow :-
https://github.com/Radioactive92177/YouPy.git
''')

url = input("Please provide the url of the video : )
"""url = "https://www.youtube.com/watch?v=-XaVelaRiiw""""

yt = YouTube(url)

print(f"Video title : {yt.title}")
print("")


video = yt.streams.first()

video.download('/Downloads')