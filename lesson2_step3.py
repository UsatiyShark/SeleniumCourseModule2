from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    sum_result = int(num1) + int(num2)
    print(sum_result)

    select=Select(browser.find_element(By.TAG_NAME,"select"))
    select.select_by_visible_text(str(sum_result))


    button = browser.find_element(By.XPATH,"//button[text()='Submit']")
    button.click()

finally:
    time.sleep(30)
    browser.quit()