import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://selenium1py.pythonanywhere.com/ru/")

try:
    browser.find_element_by_id("login_link").click()
    time.sleep(1)

    # заполняем поля
    input1 = browser.find_element_by_id("id_login-username")
    input1.clear()
    input1.send_keys("Dima@test.ru")
    input2 = browser.find_element_by_id("id_login-password")
    input2.clear()
    input2.send_keys("dimatest123")
    browser.find_element_by_name("login_submit").click()

    # проверяем, что на странице есть сообщение "Рады видеть вас снова"
    assert browser.find_element_by_css_selector(".alertinner").text == "Рады видеть вас снова"

finally:
    # выходим из учетной записи
    browser.find_element_by_id("logout_link").click()
    browser.quit()

