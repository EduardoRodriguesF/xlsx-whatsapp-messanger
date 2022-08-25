from time import sleep
from utils.access_chat import access_chat
from utils.send_from_directory import send_from_directory

def deliver_to_phone(phone):
    access_chat(phone)

    send_from_directory('messages')

def deliver_to_list(phone_list):
    for phone in phone_list:
        deliver_to_phone(phone)

        sleep(2)
