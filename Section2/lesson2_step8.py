from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name('firstname')
    input1.send_keys("Oleg")

    input2 = browser.find_element_by_name('lastname')
    input2.send_keys("Zharov")

    input3 = browser.find_element_by_name('email')
    input3.send_keys("Oleg@example.com")

    input4 = browser.find_element_by_id('file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    input4.send_keys(file_path)

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
# import os
#
# try:
#     browser = webdriver.Chrome()
#     browser.get('http://suninjuly.github.io/file_input.html')
#     current_dir = os.path.abspath(os.path.dirname(__file__))
#     file_path = os.path.join(current_dir, 'file.txt')
#
#     selector = ["[name = 'firstname']", "[name='lastname']", "[name='email']", "[name='file']"]
#     answers = ['first_name', 'second_name', 'e_mail@mail.ru',file_path]
#
#     for k, v in enumerate(selector):
#         browser.find_element(By.CSS_SELECTOR, v).send_keys(answers[k])
#
#     submit_button=browser.find_element(By.TAG_NAME, 'button').click()
# finally:
#     sleep(5)
#     browser.quit()

#one more
# import os
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# url = "http://suninjuly.github.io/file_input.html"
#
# try:
#     driver.get(url)
#
#     current_dir = os.path.abspath(os.path.dirname(__file__))
#     file_path = os.path.join(current_dir, "filetest.txt")
#
#     driver.find_element(By.NAME, "firstname").send_keys("** Name **")
#     driver.find_element(By.NAME, "lastname").send_keys("** Last name **")
#     driver.find_element(By.NAME, "email").send_keys("** This is email **")
#     time.sleep(1)
#     driver.find_element(By.ID, "file").send_keys(file_path)
#     driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
#
# except Exception as er:
#     print("*** ОШИБКА ***", er)
# finally:
#     time.sleep(7)
#     driver.quit()

