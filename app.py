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

#url = input("Please provide the url of the video : ")


validInputs = ['Y','N','y','n']
while True:
    url = input("Please provide the url of the video : ")

    yt = YouTube(url)

    print(f"Video title : {yt.title}")
    print("")

    choice = input('Is this the video? y/n : ')

    if choice in validInputs:
        if choice.lower() == 'y':
            print('Please wait,initializig download...')
            video = yt.streams.first()
            
            print("Downloading video...")
            video.download('Downloads')

            print('Video downloaded in Downloads')
            print('Thank you for using the software')
            break
        else:
            print("Please make sure to the validity of the url")
            continue
    else:
        print('Invalid input')