from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# Получаем в переменную browser указатель на браузер
browser = webdriver.Chrome()

# Переходим на страницу, на которой находится форма для авторизации
browser.get('https://www.figma.com/login')

# заполняем поле логин, привязываемся к элементу через его имя
username = browser.find_element(by=By.ID, value='email')
username.send_keys('karpovarsenij11@gmail.com')
password = browser.find_element(by=By.ID, value='current-password')
password.send_keys('ask08062004')
button = browser.find_element(by=By.CSS_SELECTOR, value='[type="submit"]')
# Нажимаем на кнопку входа
button.click()


# # заполняем поле пароля, привязываемся к элементу через его id
# password=browser.find_element(by=By.ID, value='password')
# password.send_keys('ksv30031959')

# #Получаем указатель на кнопку "Вход", привязываемся к элементу через его css_selector
# button=browser.find_element(by=By.CSS_SELECTOR, value='#loginbtn')
# #Нажимаем на кнопку входа
# button.click()
try:
    # Проверка что на странице присутствует пол
    # ное имя пользователя
    assert "Filter"
    print('The test was completed successfully')
except Exception as err:
    print('The test was failled')
# Закрываем браузер
browser.close()
