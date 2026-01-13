from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Cоздаем переменную browser из ссылки
    browser = webdriver.Chrome()
    browser.get(link)

    #Нажимаем на кнопку перехода
    browser.find_element(By.CSS_SELECTOR, "button.trollface").click()

    #Переключаемся на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Находим значение x на странице
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    # Вычисляем ответ по формуле
    y = calc(x)
    # Отправляем ответ
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)

    # Нажимаем на кнопку Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()