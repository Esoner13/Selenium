from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    submit = browser.find_element(By.TAG_NAME, 'button')
    submit.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element(By.ID, "input_value")
    x = x.text
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(str(y))
    submit = browser.find_element(By.TAG_NAME, 'button')
    submit.click()

finally:
   time.sleep(10)
   browser.quit()