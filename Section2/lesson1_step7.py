import math
import time

from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link ="http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("treasure")
x = x_element.get_attribute("valuex")
y = calc(x)

answer = browser.find_element_by_id("answer").send_keys(y)

option1 = browser.find_element_by_id("robotCheckbox")
option1.click()

option2 = browser.find_element_by_id("robotsRule")
option2.click()

button = browser.find_element_by_class_name("btn.btn-default")
button.click()

time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()

# option
# from selenium import webdriver
# from math import log, sin
#
# browser = webdriver.Chrome()
#
# # Открыть страницу http://suninjuly.github.io/get_attribute.html
# browser.get('http://suninjuly.github.io/get_attribute.html')
#
# # Найти на ней элемент-картинку/ Взять у этого элемента значение атрибута valuex
# valuex = browser.find_element_by_css_selector('[id = "treasure"]').get_attribute('valuex')
#
# # Посчитать математическую функцию от x, Ввести ответ в текстовое поле.
# browser.find_element_by_id('answer').send_keys(str(log(abs(12 * sin(int(valuex))))))
#
# # Отметить checkbox "Подтверждаю, что являюсь роботом". Выбрать radiobutton "Роботы рулят!". Нажать на кнопку Отправить.
# for selector in ['#robotCheckbox', '#robotsRule', '.btn.btn-default']:
#   browser.find_element_by_css_selector(selector).click()
