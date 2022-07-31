from selenium import webdriver

driver = webdriver.Chrome()

def getChatUrl(phone):
    return 'https://web.whatsapp.com/send?phone={}&text&type=phone_number&app_absent=0'.format(phone)


driver.get(getChatUrl('5513997406352'))

