import os
from time import sleep
from utils.send_message import send_message
from utils.attachments import send_image

def send_from_directory(directory):
    for filename in sorted(os.listdir(directory)):
        file = os.path.join(directory, filename)

        if '.txt' in filename:
            with open(file) as f:
                send_message(f.read())
        else:
            send_image(file)
            sleep(3)
