from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Получаем в переменную browser указатель на браузер
browser = webdriver.Chrome()

# Переходим на страницу, на которой находится форма для авторизации
browser.get('https://www.figma.com/login')

# заполняем поле логин, привязываемся к элементу через его имя
username = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'email')))
username.send_keys('karpovarsenij11@gmail.com')
password = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'current-password')))
password.send_keys('ask08062004')
button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '[type="submit"]')))
# Нажимаем на кнопку входа
button.click()

# Ожидание загрузки страницы после авторизации
WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"a.new_file_creation_topbar--tile--KkIyp.text--fontPos13--5OfL8.text--_fontBase--VaHfk:nth-child(1)")))

# Нажимаем на кнопку "New File" для создания нового документа
design = browser.find_element(
    By.CSS_SELECTOR, "a.new_file_creation_topbar--tile--KkIyp.text--fontPos13--5OfL8.text--_fontBase--VaHfk:nth-child(1)")
design.click()

# Проверка, что на странице присутствует текст "Untitled"
try:
    untitled_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.ksGmeU")))
    assert "Untitled" in untitled_element.text
    print('The test was completed successfully')
except Exception as err:
    print('The test was failed: ' + str(err))

# Закрываем браузер
browser.quit()
