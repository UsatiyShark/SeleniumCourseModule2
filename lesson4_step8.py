from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math
import time

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    button = browser.find_element(By.XPATH, "//button[text()='Book']")
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
    )
    button.click()

    #
    def calc(x):
         return str(math.log(abs(12 * math.sin(int(x)))))
    #
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    #
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    #
    #
    button = browser.find_element(By.XPATH,"//button[text()='Submit']")
    button.click()

finally:
    time.sleep(30)
    browser.quit()