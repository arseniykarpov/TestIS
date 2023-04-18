from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Получаем в переменную browser указатель на браузер
browser = webdriver.Chrome()

# Переходим на страницу, на которой находится форма для авторизации
browser.get('https://www.figma.com/login')

# заполняем поле логин, привязываемся к элементу через его имя
username = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'email')))
username.send_keys('karpovarsenij11@gmail.com')
password = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'current-password')))
password.send_keys('ask08062004')
button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[type="submit"]')))
# Нажимаем на кнопку входа
button.click()

# Нажимаем на кнопку "Community"
button_profile = browser.find_element(By.CSS_SELECTOR, 'button[data-testid="ProfileButton"]')
button_profile.click()
button_plugin = browser.find_element(By.XPATH, "//div[@class='scroll_container--scrollContainer--WKNyX scroll_container--full--S7bP3']/div[@class='scroll_container--full--S7bP3']/div/div/div[@id='undefined-undefined-3']")
button_plugin.click()

try:
    untitled_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.ksGmeU")))
    assert "Noise" in untitled_element.text
    print('The test was completed successfully')
except Exception as err:
    print('The test was failed: ' + str(err))

# Закрываем браузер
browser.quit()
