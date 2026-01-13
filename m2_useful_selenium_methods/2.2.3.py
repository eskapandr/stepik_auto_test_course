from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects2.html"

try:
    # Cоздаем переменную browser из ссылки
    browser = webdriver.Chrome()
    browser.get(link)
    # вычисляем значение
    first_num = browser.find_element(By.CSS_SELECTOR, "#num1").text
    second_num = browser.find_element(By.CSS_SELECTOR, "#num2").text
    sum = int(first_num) + int(second_num)
    # выбираем значение в выпадающем списке
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(sum))
    # отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()