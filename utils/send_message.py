from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.wait_element import wait_element

def send_message(message):
    textbox = wait_element(By.CSS_SELECTOR, '[data-testid="conversation-panel-wrapper"] [role="textbox"][contenteditable]')

    return textbox.send_keys(message + Keys.ENTER)
