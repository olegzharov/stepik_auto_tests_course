from selenium import webdriver, common
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    #link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector("html body.bg-light div.container form div.first_block div.form-group.first_class input.form-control.first").send_keys("First")
    browser.find_element_by_css_selector("html body.bg-light div.container form div.first_block div.form-group.second_class input.form-control.second").send_keys("Second")
    browser.find_element_by_css_selector("html body.bg-light div.container form div.first_block div.form-group.third_class input.form-control.third").send_keys("Third")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

except common.exceptions.NoSuchElementException:
    print("Oops!  Something wrong with this forms.")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
