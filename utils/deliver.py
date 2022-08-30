from time import sleep
from utils.access_chat import access_chat
from utils.send_from_directory import send_from_directory

def deliver_to_phone(phone):
    is_chat_available = access_chat(phone)

    if not is_chat_available:
        print('Unavailable chat:', phone)
        return False

    send_from_directory('messages')
    return True

def deliver_to_list(phone_list):
    for phone in phone_list:
        deliver_to_phone(phone)

        sleep(2)
