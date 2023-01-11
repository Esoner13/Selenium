import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

try:

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x1 = browser.find_element(By.ID, "input_value")
    x1 = x1.text
    y = calc(x1)

#    button = browser.find_element(By.TAG_NAME, "button")
#    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(str(y))
    browser.execute_script("window.scrollBy(0, 100);")

    robot = browser.find_element(By.CSS_SELECTOR, '[id=robotCheckbox]')
    robot.click()
    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()

finally:
   time.sleep(10)
   browser.quit()
