import re

def is_phone_valid(phone):
    return len(phone) <= 13

def sanitize_phone(phone):
    if (len(phone) < 3): return ''

    result = re.sub('[^0-9]', '', phone)

    if (result[0] != '5' or result[1] != '5'):
        result = '55' + result

    return result
