from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from driver import driver

def wait_element(by, selector):
    try: 
        try:
            fallback_element = driver.find_element(By.CSS_SELECTOR, '[role="button"][data-testid="popup-controls-ok"]')
            return False
        except NoSuchElementException:
            return driver.find_element(by, selector)
    except NoSuchElementException:
        sleep(.2)
        return wait_element(by, selector)
