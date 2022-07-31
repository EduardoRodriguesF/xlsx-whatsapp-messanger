from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

driver = webdriver.Chrome()

def get_chat_url(phone):
    return 'https://web.whatsapp.com/send?phone={}&text&type=phone_number&app_absent=0'.format(phone)

def get_textbox():
    return driver.find_element(By.CSS_SELECTOR, '[data-testid="conversation-panel-wrapper"] [role="textbox"][contenteditable]')

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

def message_phone(phone):
    driver.get(get_chat_url(phone))

    textbox = wait_textbox()

    print(textbox)



message_phone('5513997406352')
