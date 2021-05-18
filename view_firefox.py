# view_driver1 = webdriver.Firefox(executable_path="D:/For Chrome/geckodriver")

import time
from selenium import webdriver
from time import sleep
import random

source_list = []
FILE_NAME = 'source.txt'

with open(FILE_NAME, 'r', encoding='utf-8') as f:
    for line in f:
        source_list.append(line)

source_list = [line.rstrip('\n') for line in open(FILE_NAME)]

view_driver1 = webdriver.Firefox(executable_path="D:/For Chrome/geckodriver")
view_driver2 = webdriver.Firefox(executable_path="D:/For Chrome/geckodriver")
view_driver3 = webdriver.Firefox(executable_path="D:/For Chrome/geckodriver")
view_driver4 = webdriver.Firefox(executable_path="D:/For Chrome/geckodriver")
view_driver5 = webdriver.Firefox(executable_path="D:/For Chrome/geckodriver")

while True:
    view_driver1.get(random.choice(source_list))
    time.sleep(random.randint(3, 60))

    view_driver2.get(random.choice(source_list))
    time.sleep(random.randint(3, 60))

    view_driver3.get(random.choice(source_list))
    time.sleep(random.randint(3, 60))

    view_driver4.get(random.choice(source_list))
    time.sleep(random.randint(3, 60))

    view_driver5.get(random.choice(source_list))
    time.sleep(random.randint(3, 60))

    sleep(random.randint(60, 120))

    view_driver1.refresh()

    view_driver2.refresh()

    view_driver3.refresh()

    view_driver4.refresh()

    view_driver5.refresh()
