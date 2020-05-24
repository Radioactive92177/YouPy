validInputs = ['Y','N','y','n']

while True:
    url = input('Please provide url of the video: ')
    choice = input('Is this the video? y/n : ')

    if choice in validInputs:
        if choice.lower() == 'y':
            print('You said yes')
            print("Downloading video")
            break
        else:
            print("Please make sure to the validity of the url")
            continue
    else:
        print('Invalid input')