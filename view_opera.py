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

while True:
    view_driver1 = webdriver.Opera(executable_path="D:/For Chrome/operadriver")
    view_driver2 = webdriver.Opera(executable_path="D:/For Chrome/operadriver")
    view_driver3 = webdriver.Opera(executable_path="D:/For Chrome/operadriver")
    view_driver4 = webdriver.Opera(executable_path="D:/For Chrome/operadriver")
    view_driver5 = webdriver.Opera(executable_path="D:/For Chrome/operadriver")

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

    view_driver1.quit()
    time.sleep(random.randint(10, 30))

    view_driver2.quit()
    time.sleep(random.randint(10, 30))

    view_driver3.quit()
    time.sleep(random.randint(10, 30))

    view_driver4.quit()
    time.sleep(random.randint(10, 30))

    view_driver5.quit()
    time.sleep(random.randint(10, 30))
