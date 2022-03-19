import math
import time

from selenium.webdriver.support.ui import Select
from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link ="http://suninjuly.github.io/selects2.html"

browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("num1")
x = x_element.text
y_element = browser.find_element_by_id("num2")
y = y_element.text
my_sum = int(x) + int(y)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(my_sum))

button = browser.find_element_by_class_name("btn.btn-default")
button.click()

time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()

# import time
# from selenium.webdriver.support.ui import Select
# from selenium import webdriver
#
# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/selects1.html")
#
#     a = browser.find_element_by_css_selector("#num1").text
#     b = browser.find_element_by_css_selector("#num2").text
#     x = int(a) + int(b)
#
#
#     time.sleep(1)
#
#     Select(browser.find_element_by_tag_name("select")).select_by_value(str(x))
#     browser.find_element_by_css_selector("[type='submit']").click()
#
# finally:
#     time.sleep(10)
#     browser.quit()
