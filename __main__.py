from utils.xlsx import for_each_valid_phone
from utils.access_chat import access_chat
from time import sleep

if __name__ == '__main__':
    def callback(phone):
        access_chat(phone)
        sleep(10)

    for_each_valid_phone(callback)
