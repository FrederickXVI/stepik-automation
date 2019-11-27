import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://selenium1py.pythonanywhere.com/ru/catalogue/")

try:
    btnlist = browser.find_elements_by_css_selector("form .btn-primary")

    # кликаем на первые 3 кнопки "Добавить в корзину"
    for n in range(3):
        time.sleep(1)
        btnlist[n].click()
        btnlist = browser.find_elements_by_css_selector("form .btn-primary")

    # переходим в корзину
    browser.get("http://selenium1py.pythonanywhere.com/ru/basket/")

    # посчитаем количество товаров
    qtylist = browser.find_elements_by_css_selector(".input-group input")
    qty = 0
    for i in range(len(qtylist)):
        qty = qty + int(qtylist[i].get_attribute("value"))

    # проверяем, что количество товара равно 3
    assert qty == 3

finally:
    browser.quit()
