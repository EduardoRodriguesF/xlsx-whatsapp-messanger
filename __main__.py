from utils.xlsx import for_each_valid_phone
from utils.deliver import deliver_to_phone
from time import sleep

if __name__ == '__main__':
    for_each_valid_phone(deliver_to_phone)
