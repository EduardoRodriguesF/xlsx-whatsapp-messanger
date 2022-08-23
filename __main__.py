import os
from time import sleep
from utils.access_chat import access_chat
from utils.send_message import send_message
from utils.attachments import send_image

def deliver_to_phone(phone):
    access_chat(phone)

    directory = 'messages'
    for filename in sorted(os.listdir(directory)):
        file = os.path.join(directory, filename)

        if '.txt' in filename:
            with open(file) as f:
                send_message(f.read())
        else:
            send_image(file)
            sleep(2)

if __name__ == '__main__':
    deliver_to_phone('5513997406352')
