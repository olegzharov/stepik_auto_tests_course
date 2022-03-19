import math
import time

from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link ="http://SunInJuly.github.io/execute_script.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(y)

    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    browser.execute_script("return arguments[0].scrollIntoView(true);",
                           option1)
    option1.click()

    option2 = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);",
                           option2)
    option2.click()

    button = browser.find_element_by_class_name("btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# another option
# from selenium import webdriver
# from math import log, sin
#
# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/math.html")
#
# x = browser.find_element_by_css_selector('[id = "input_value"]').text
# browser.find_element_by_css_selector('[id = "answer"]').send_keys(str(log(abs(12 * sin(int(x))))))
#
# for selector in ['[for="robotCheckbox"]', '[for="robotsRule"]', '.btn']:
#     browser.find_element_by_css_selector(selector).click()

# import math
#
# from selenium import webdriver
#
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
#
# def print_answer(remote: webdriver.Remote):
#     alert = remote.switch_to.alert
#     print(alert.text.split()[-1])
#     alert.accept()
#
#
# browser = webdriver.Chrome()
# link = "http://suninjuly.github.io/math.html"
# browser.get(link)
#
# try:
#     x_element = browser.find_element_by_id("input_value").text
#     browser.find_element_by_id("answer").send_keys(calc(x_element))
#     elements_to_select = tuple(("[id = 'robotCheckbox']", "[for=\"robotsRule\"]", "button.btn.btn-default"))
#
#     for elem in elements_to_select:
#         browser.find_element_by_css_selector(elem).click()
#
#     print_answer(browser)
# finally:
#     browser.quit()

# from selenium.webdriver.chrome.webdriver import WebDriver
# import math
#
#
# # прописываем функцию для подсчета значения
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
#
# # открываем браузер
# con = WebDriver()
#
# # открываем целевую страницу
# con.get("http://suninjuly.github.io/math.html")
#
# # находим веб-элемент x
# web_element_x = con.find_element_by_css_selector("#input_value")
#
# # считываем значение элемента x
# x_int = int(web_element_x.text)
#
# # находим значение для ввода
# value = calc(x_int)
#
# # находим элементы текстовое поле, чекбокс, радио-кнопку, кнопку "отправить"
# text_field = con.find_element_by_css_selector("#answer")
# checkbox = con.find_element_by_css_selector("#robotCheckbox")
# radio_btn = con.find_element_by_css_selector("#robotsRule")
# submit_btn = con.find_element_by_css_selector('[type="submit"]')
#
# # вводим значение в текстовое поле
# text_field.send_keys(value)
#
# # отмечаем чекбокс
# checkbox.click()
#
# # выбираем значение радио-кнопки
# radio_btn.click()
#
# # нажимаем на кнопку "отправить"
# submit_btn.click()
#
# # закрываем браузер
# con.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import math, time
#
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
# link = "http://suninjuly.github.io/math.html"
#
# with webdriver.Chrome() as browser:
#     # 1
#     browser.get(link)
#     # 2-4
#     x_element = browser.find_element_by_id("input_value")
#     x = x_element.text
#     y = calc(x)
#     input1 = browser.find_element_by_id ("answer")
#     input1.send_keys(str(y))
#     # 5
#     ch1 = browser.find_element_by_id ("robotCheckbox")
#     ch1.click()
#     # 6
#     r1 = browser.find_element_by_id ("robotsRule")
#     r1.click()
#     # 7
#     button = browser.find_element_by_css_selector(".btn")
#     button.click()
#     time.sleep(10)
