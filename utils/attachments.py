import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.wait_element import wait_element


def open_clip():
    clip = wait_element(By.CSS_SELECTOR, '[data-testid="conversation-clip"] [role="button"]')

    clip.click()

def send_image(image):
    open_clip()
    image_abs = os.path.abspath(image)

    attach_media_button = wait_element(By.CSS_SELECTOR, '[data-testid="mi-attach-media"] input[type="file"]')
    attach_media_button.send_keys(image_abs)

    send_button = wait_element(By.CSS_SELECTOR, '.copyable-area [role="button"] [data-testid="send"]')
    send_button.click()
