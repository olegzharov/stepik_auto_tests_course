from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(5)
    browser.quit()

# Better with:
# with webdriver.Chrome() as browser:
#     browser.get(link)
#     button = browser.find_element(By.ID, "submit")
#     button.click()
