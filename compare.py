import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

try:

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "book")

    WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, 'price'), "100"))
    button.click()

    x1 = browser.find_element(By.ID, "input_value")
    x1 = x1.text
    y = calc(x1)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(str(y))
    button1 = browser.find_element(By.ID, "solve")
    button1.click()

finally:
    time.sleep(15)
    browser.quit()
