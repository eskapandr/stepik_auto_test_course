from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "https://SunInJuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    # Cоздаем переменную browser из ссылки
    browser = webdriver.Chrome()
    browser.get(link)
    # Считываем значение переменной x и считаем математическую функцию от x
    x = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)
    y = calc(x)
    # cкроллим страницу вниз
    browser.execute_script("window.scrollBy(0, 100);")
    # отправляем ответ
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
    # Кликаем сheckbox
    browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']").click()
    # Кликаем radiobutton
    browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()
    # Отправляем заполненную форму
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
