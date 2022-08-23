from utils.access_chat import access_chat
from utils.send_message import send_message
from utils.attachments import send_image

def deliver_to_phone(phone):
    access_chat(phone)

    send_message('teste drive')
    send_image('./message/example.jpg')

if __name__ == '__main__':
    deliver_to_phone('5513997406352')
