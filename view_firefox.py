from selenium import webdriver
import time
import random

while True:
    view_driver1 = webdriver.Firefox()
    view_driver1.get("https://habr.com/ru/post/481074/")

    time.sleep(random.randint(60, 120))

    view_driver1.quit()