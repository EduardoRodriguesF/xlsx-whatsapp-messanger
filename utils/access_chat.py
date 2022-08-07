from driver import driver

def access_chat(phone):
    url = 'https://web.whatsapp.com/send?phone={}&text&type=phone_number&app_absent=0'.format(phone)
    return driver.get(url)
