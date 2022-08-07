import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from driver import driver
from utils.access_chat import access_chat
from utils.wait_element import wait_element
from utils.send_message import send_message
from utils.attachments import send_image

def deliver_to_phone(phone):
    access_chat(phone)

    send_message('teste drive')
    send_image('./message/example.jpg')

deliver_to_phone('5513997406352')
