import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://selenium1py.pythonanywhere.com/ru/")

try:
    browser.find_element_by_id("login_link").click()
    link = browser.current_url

    # отключаем атрибут required для полей "Адрес электронной почты" и "Пароль"
    browser.execute_script("document.querySelector('#id_login-username').removeAttribute('required')")
    browser.execute_script("document.querySelector('#id_login-password').removeAttribute('required')")

    time.sleep(1)
    input1 = browser.find_element_by_id("id_login-username")
    input1.clear()
    input2 = browser.find_element_by_id("id_login-password")
    input2.clear()
    button = browser.find_element_by_name("login_submit")
    button.click()

    alert = browser.find_element_by_css_selector(".alert")

    # проверяем, что остались на той же странице и сообщение об ошибке отображается
    assert browser.current_url == link and alert.is_displayed()

finally:
    browser.quit()

