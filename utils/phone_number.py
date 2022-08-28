import re

def is_phone_valid(phone):
    if not phone: return False

    result = phone.split('/')[0].strip()

    return len(result) == 13 or len(result) == 12

def sanitize_phone(phone):
    phone = str(phone)

    if (len(phone) < 3): return ''

    result = re.sub('[^0-9]', '', phone)

    if not result: return ''

    if (result[0] != '5'):
        result = '55' + result

    return result
