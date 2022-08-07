from selenium.common.exceptions import NoSuchElementException
from time import sleep
from driver import driver

def wait_element(by, selector):
    try: 
        return driver.find_element(by, selector)
    except NoSuchElementException:
        sleep(.2)
        return wait_element(by, selector)
