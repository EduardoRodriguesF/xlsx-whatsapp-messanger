from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

driver = webdriver.Chrome()

def get_chat_url(phone):
    return 'https://web.whatsapp.com/send?phone={}&text&type=phone_number&app_absent=0'.format(phone)

def get_textbox():
    return driver.find_element(By.CSS_SELECTOR, '[data-testid="conversation-panel-wrapper"] [role="textbox"][contenteditable]')

def access_chat(phone):
    return driver.get(get_chat_url(phone))

def wait_textbox():
    try:
        textbox = get_textbox()

        print('Chat encontrado!')
        return textbox
    except NoSuchElementException:
        print('Erro ao tentar acessar a caixa de texto')
        print('tentando novamente em alguns segundos...\n')

        sleep(3)

        return wait_textbox()

def send_message(message, textbox):
    textbox.send_keys(message + Keys.ENTER)


def message_phone(phone):
    access_chat(phone)

    textbox = wait_textbox()

    send_message('teste drive', textbox)



message_phone('5513997406352')
