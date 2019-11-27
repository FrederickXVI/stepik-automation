from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://selenium1py.pythonanywhere.com/ru/")
password = "dimatest123"
login = "Dima@test.ru"

try:
    browser.find_element_by_id("login_link").click()
    time.sleep(1)

    input1 = browser.find_element_by_name("registration-email")
    input1.clear()
    input1.send_keys(login)
    input2 = browser.find_element_by_name("registration-password1")
    input2.clear()
    input2.send_keys(password)
    input3 = browser.find_element_by_name("registration-password2")
    input3.clear()
    input3.send_keys(password)
    browser.find_element_by_name("registration_submit").click()

    # проверяем, что на странице есть сообщение "Спасибо за регистрацию!"
    assert browser.find_element_by_css_selector(".alertinner").text == "Спасибо за регистрацию!"

finally:
    # переходим на страницу аккаунта
    browser.get("http://selenium1py.pythonanywhere.com/ru/accounts/profile/")
    # клик на кнопку "Удалить профайл"
    browser.find_element_by_id("delete_profile").click()
    time.sleep(1)
    browser.find_element_by_id("id_password").send_keys(password)
    browser.find_element_by_css_selector(".btn-danger").click()
    browser.quit()

