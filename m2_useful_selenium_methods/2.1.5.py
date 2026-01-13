from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "https://suninjuly.github.io/math.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Cоздаем переменную browser из ссылки
    browser = webdriver.Chrome()
    browser.get(link)
    # Находим значение x на странице
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    # Вычисляем ответ по формуле
    y = calc(x)
    # Отправляем ответ
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
    # Кликаем сheckbox
    option_checkbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    option_checkbox.click()
    # Кликаем radiobutton
    option_radiobutton = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    option_radiobutton.click()
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()