from driver import driver
from utils.wait_element import wait_element
from selenium.webdriver.common.by import By

def access_chat(phone):
    url = 'https://web.whatsapp.com/send?phone={}&text&type=phone_number&app_absent=0'.format(phone)

    driver.get(url)

    chat_confirmation = wait_element(By.CSS_SELECTOR, '[data-testid="conversation-panel-wrapper"] [role="textbox"][contenteditable]')

    return bool(chat_confirmation)
