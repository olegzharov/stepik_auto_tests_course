from selenium import webdriver
import time

# link = "http://suninjuly.github.io/simple_form_find_task.html"
# link ="http://suninjuly.github.io/find_link_text_redirect13.html"
link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name('city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")
    # button = browser.find_element_by_css_selector("button.btn")
    button = browser.find_element_by_xpath("/html/body/div/form/div[6]/button[3]")
    # Решение №1 (тривиальное)
    # buttons = driver.find_elements_by_xpath("//button[text()='Submit']")
    # # решение № 2
    # buttons = driver.find_elements_by_xpath("//button")
    # for button in buttons:
    #     if button.text == 'Submit':
    #         button.click()
    #3
    # browser.find_element_by_xpath('//*[@type="submit"]').click()
    #4
    #button = browser.find_element_by_xpath('//button[@type="submit"]')
    
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# another example
# from selenium import webdriver
# import time
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
# link_login = "https://stepik.org/"
# link_answer = "https://stepik.org/lesson/138920/step/4?unit=196194"
#
# try:
#     # get verification code
#     browser = webdriver.Firefox()
#     browser.get(link)
#
#     first_name = "first_name"
#     last_name = "last_name"
#     city = "city"
#     country = "country"
#
#     input1 = browser.find_element_by_tag_name("input")
#     input1.send_keys(first_name)
#     input2 = browser.find_element_by_name("last_name")
#     input2.send_keys(last_name)
#     input3 = browser.find_element_by_class_name("city")
#     input3.send_keys(city)
#     input4 = browser.find_element_by_id("country")
#     input4.send_keys(country)
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
#     alert = browser.switch_to.alert
#     text_alert = alert.text
#     answer_value = text_alert[(text_alert.index(': '))+2:]
#     time.sleep(5)
#     alert.accept()
#
#     # log in
#     browser.get(link_login)
#     time.sleep(5)
#
#     submit_button = browser.find_element_by_css_selector(".navbar__auth")
#     submit_button.click()
#
#     login_email = "e-mail"
#     login_password = "password"
#
#     s_username = browser.find_element_by_id("id_login_email")
#     s_username.send_keys(login_email)
#
#     s_password = browser.find_element_by_id("id_login_password")
#     s_password.send_keys(login_password)
#
#     button = browser.find_element_by_css_selector(".sign-form__btn")
#     button.click()
#
#     time.sleep(5)
#
#     # input verification code in textarea
#     browser.get(link_answer)
#     time.sleep(5)
#
#     textarea = browser.find_element_by_css_selector(".textarea")
#     textarea.send_keys(answer_value)
#     time.sleep(5)
#
#     submit_button = browser.find_element_by_css_selector(".submit-submission")
#     submit_button.click()
#     time.sleep(5)
#
# finally:
#     time.sleep(1)
#     # close browser
#     browser.quit()
