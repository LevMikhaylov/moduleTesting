import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

# Настройка драйвера Firefox
@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.headless = False  # Для отображения браузера (True для безголового режима)
    service = Service(executable_path='C:\\Users\\Student\\Downloads\\geckodriver-v0.26.0-win64\\geckodriver.exe')  # Укажите путь до geckodriver
    driver = webdriver.Firefox(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_product_images(driver):
    # Открытие сайта и клик по первому продукту
    driver.get("https://demo.opencart.com/")
    first_product = driver.find_element(By.XPATH, '//div[@class="product-layout product-grid"]//a')
    first_product.click()
    
    # Проверка переключения скриншотов на странице продукта
    time.sleep(2)
    screenshot_thumbnails = driver.find_elements(By.XPATH, '//div[@id="content"]//ul[@class="thumbnails"]/li')
    assert len(screenshot_thumbnails) > 1, "Скриншоты не переключаются на странице продукта."

def test_currency_switch(driver):
    # Смена валюты с доллара на евро и обратно
    driver.get("https://demo.opencart.com/")
    
    currency_dropdown = driver.find_element(By.XPATH, '//div[@class="btn-group"]/button')
    currency_dropdown.click()

    # Выбрать евро
    euro_currency = driver.find_element(By.XPATH, '//button[@name="EUR"]')
    euro_currency.click()
    
    time.sleep(2)
    
    # Вернуться к доллару
    currency_dropdown.click()
    dollar_currency = driver.find_element(By.XPATH, '//button[@name="USD"]')
    dollar_currency.click()

def test_pc_category(driver):
    # Переход в категорию PC и проверка, что страница пуста
    driver.get("https://demo.opencart.com/")
    menu_pc = driver.find_element(By.XPATH, '//ul[@class="nav navbar-nav"]/li/a[contains(text(), "PC")]')
    menu_pc.click()
    
    time.sleep(2)
    
    page_content = driver.find_element(By.XPATH, '//div[@id="content"]')
    assert "There are no products to list in this category." in page_content.text, "Страница категории PC не пуста."

def test_register(driver):
    # Переход в регистрацию, заполнение формы и регистрация
    driver.get("https://demo.opencart.com/")
    menu_register = driver.find_element(By.XPATH, '//ul[@class="nav navbar-nav"]/li/a[contains(text(), "Register")]')
    menu_register.click()

    first_name = driver.find_element(By.ID, 'input-firstname')
    last_name = driver.find_element(By.ID, 'input-lastname')
    email = driver.find_element(By.ID, 'input-email')
    telephone = driver.find_element(By.ID, 'input-telephone')
    password = driver.find_element(By.ID, 'input-password')
    confirm_password = driver.find_element(By.ID, 'input-confirm')
    
    first_name.send_keys('John')
    last_name.send_keys('Doe')
    email.send_keys('john.doe@example.com')
    telephone.send_keys('1234567890')
    password.send_keys('Password123')
    confirm_password.send_keys('Password123')

    agree_checkbox = driver.find_element(By.NAME, 'agree')
    agree_checkbox.click()

    register_button = driver.find_element(By.XPATH, '//input[@value="Continue"]')
    register_button.click()

    time.sleep(2)

def test_search(driver):
    # Поиск по слову в строке поиска
    driver.get("https://demo.opencart.com/")
    search_box = driver.find_element(By.NAME, 'search')
    search_box.send_keys('Laptop')  # Вводим слово "Laptop"
    search_box.send_keys(Keys.RETURN)  # Нажимаем Enter для поиска

    time.sleep(3)

    search_results = driver.find_element(By.XPATH, '//div[@id="content"]')
    assert "No products were found" not in search_results.text, "Продукты не найдены."
