import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://selenium1py.pythonanywhere.com/ru/")

try:
    browser.find_element_by_id("login_link").click()
    link = browser.current_url

    # отключаем атрибут required для полей "Адрес электронной почты", "Пароль" и "Повторите пароль"
    browser.execute_script("document.querySelector('#id_registration-email').removeAttribute('required')")
    browser.execute_script("document.querySelector('#id_registration-password1').removeAttribute('required')")
    browser.execute_script("document.querySelector('#id_registration-password2').removeAttribute('required')")

    time.sleep(1)
    input1 = browser.find_element_by_id("id_registration-email")
    input1.clear()
    input2 = browser.find_element_by_id("id_registration-password1")
    input2.clear()
    input3 = browser.find_element_by_id("id_registration-password2")
    input3.clear()
    button = browser.find_element_by_name("registration_submit")
    button.click()

    alert = browser.find_element_by_css_selector(".alert")

    # проверяем, что остались на той же странице и сообщение об ошибке отображается
    assert browser.current_url == link and alert.is_displayed()

finally:
    browser.quit()

