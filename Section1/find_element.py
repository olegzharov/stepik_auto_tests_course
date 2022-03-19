from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/simple_form_find_task.html")
button = browser.find_element_by_id("submit_button")

# find_element_by_id — поиск по уникальному атрибуту id элемента. Если ваши разработчики проставляют всем элементам в приложении уникальный id, то вам повезло, и вы чаще всего будет использовать этот метод, так как он наиболее стабильный;
# find_element_by_css_selector — поиск элемента с помощью правил на основе CSS. Это универсальный метод поиска, так как большинство веб-приложений использует CSS для вёрстки и задания оформления страницам. Если find_element_by_id вам не подходит из-за отсутствия id у элементов, то скорее всего вы будете использовать именно этот метод в ваших тестах;
# find_element_by_xpath — поиск с помощью языка запросов XPath, позволяет выполнять очень гибкий поиск элементов;
# find_element_by_name — поиск по атрибуту name элемента;
# find_element_by_tag_name — поиск элемента по названию тега элемента;
# find_element_by_class_name — поиск по значению атрибута class;
# find_element_by_link_text — поиск ссылки на странице по полному совпадению;
# find_element_by_partial_link_text — поиск ссылки на странице, если текст селектора совпадает с любой частью текста ссылки.

