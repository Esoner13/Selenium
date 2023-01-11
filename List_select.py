import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


try:
    link = 'https://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)
    n1 = browser.find_element(By.ID, 'num1')
    n2 = browser.find_element(By.ID, 'num2')
    n1 = n1.text
    n2 = n2.text
    z = int(n1)+int(n2)
    z = str(z)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(z)

    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
