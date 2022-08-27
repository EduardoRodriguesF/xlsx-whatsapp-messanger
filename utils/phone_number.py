import re

def is_phone_valid(phone):
    return len(phone) > 13

def sanitize_phone(phone):
    result = re.sub('[^0-9]', '', phone)

    return result
