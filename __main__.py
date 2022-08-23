from utils.access_chat import access_chat
from utils.send_from_directory import send_from_directory

def deliver_to_phone(phone):
    access_chat(phone)

    send_from_directory('messages')

if __name__ == '__main__':
    deliver_to_phone('5513997406352')
