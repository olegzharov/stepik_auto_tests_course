from selenium import webdriver
import time, math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    answer = browser.find_element_by_id("answer").send_keys(y)

    button = browser.find_element_by_class_name("btn.btn-primary")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# another
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from time import sleep
# import math
#
# try:
#     browser=webdriver.Chrome()
#     browser.get('http://suninjuly.github.io/alert_accept.html')
#     browser.find_element(By.TAG_NAME,'button').click()
#     alert = browser.switch_to.alert.accept()
#     x=browser.find_element(By.ID,'input_value').text
#     answer=browser.find_element(By.ID,'answer').send_keys(str(math.log(abs(12*math.sin(int(x))))))
#     submit=browser.find_element(By.TAG_NAME,'button').click()
#
# finally:
#     sleep(5)
#     browser.quit()

# import math
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# url = "http://suninjuly.github.io/alert_accept.html"
#
#
# def calc(x: str):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
#
# try:
#     driver.get(url)
#     # driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
#     driver.find_element(By.XPATH,
#                         "//button['I want to go on a magical journey!']").click()
#
#     confirm = driver.switch_to.alert
#     confirm.accept()
#
#     number = driver.find_element(By.ID, "input_value").text
#     driver.find_element(By.ID, "answer").send_keys(calc(number))
#     driver.find_element(By.XPATH, "//button['Submit']").click()
#
# except Exception as er:
#     print(f"*** Ошибка *** {er}")
# finally:
#     time.sleep(7)
#     driver.quit()

