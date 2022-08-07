import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

driver = webdriver.Chrome()

def wait_element(by, selector):
    try: 
        return driver.find_element(by, selector)
    except NoSuchElementException:
        sleep(.2)
        return wait_element(by, selector)

def get_chat_url(phone):
    return 'https://web.whatsapp.com/send?phone={}&text&type=phone_number&app_absent=0'.format(phone)

def open_clip():
    clip = driver.find_element(By.CSS_SELECTOR, '[data-testid="conversation-clip"] [role="button"]')

    clip.click()

    sleep(1.5)

def access_chat(phone):
    return driver.get(get_chat_url(phone))

def send_message(message, textbox):
    textbox.send_keys(message + Keys.ENTER)

def send_image(image):
    open_clip()
    image_abs = os.path.abspath(image)

    attach_media_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="mi-attach-media"] input[type="file"]')
    attach_media_button.send_keys(image_abs)

    send_button = wait_element(By.CSS_SELECTOR, '.copyable-area [role="button"] [data-testid="send"]')

    send_button.click()

def deliver_to_phone(phone):
    access_chat(phone)

    textbox = wait_element(By.CSS_SELECTOR, '[data-testid="conversation-panel-wrapper"] [role="textbox"][contenteditable]')

    send_message('teste drive', textbox)
    send_image('./message/example.jpg')

deliver_to_phone('5513997406352')
