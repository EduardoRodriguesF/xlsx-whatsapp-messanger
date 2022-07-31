from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

driver = webdriver.Chrome()

def getChatUrl(phone):
    return 'https://web.whatsapp.com/send?phone={}&text&type=phone_number&app_absent=0'.format(phone)

def getTextbox():
    return driver.find_element(By.CSS_SELECTOR, '[data-testid="conversation-panel-wrapper"] [role="textbox"][contenteditable]')

def wait_chat():
    try:
        textbox = getTextbox()

        print('Chat encontrado!')
        return
    except NoSuchElementException:
        print('Erro ao tentar acessar a caixa de texto')
        print('tentando novamente em alguns segundos...\n')

        sleep(3)

        wait_chat()

def accessChat(phone):
    driver.get(getChatUrl(phone))

    wait_chat()



accessChat('5513997406352')
