from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Ivanov")

    input2 = browser.find_element(By.NAME, "email")
    input2.send_keys("Ivan@mail.ru")

    element = browser.find_element(By.ID, "file")
    element.send_keys('/Users/ilya/PycharmProjects/module2/lesson2_step8.py')

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
finally:
    time.sleep(10)
    browser.quit()