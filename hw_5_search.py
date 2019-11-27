import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://selenium1py.pythonanywhere.com/ru/")
search_value = "hack"

try:
    input1 = browser.find_element_by_id("id_q")
    input1.clear()
    input1.send_keys(search_value)

    button = browser.find_element_by_css_selector("input.btn")
    button.click()

    elements = browser.find_elements_by_css_selector(".product_pod h3 a")

    # пройдемся по всей длине массива WebElements
    for element in range(len(elements)):
        time.sleep(2)
        # кликаем на элемент массива с текущим индексом
        elements[element].click()
        name = browser.find_element_by_css_selector(".product_main h1").text.lower()
        description = browser.find_element_by_css_selector(".product_page>p").text.lower()
        # проверим, что ключевое слово есть в имени или описании
        assert search_value in name or search_value in description
        browser.back()
        # заново инициализируем массив
        elements = browser.find_elements_by_css_selector(".product_pod h3 a")

finally:
    browser.quit()
