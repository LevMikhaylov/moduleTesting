from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

# Настройка драйвера Firefox
options = Options()
options.headless = False  # Для отображения браузера (True для безголового режима)
service = Service(executable_path='C:\\Users\\Student\\Downloads\\geckodriver-v0.26.0-win64\\geckodriver.exe')  # Укажите путь до geckodriver
driver = webdriver.Firefox(service=service, options=options)

try:
    # 1. Открыть сайт и кликнуть на продукт на главной странице
    driver.get("https://demo.opencart.com/")
    driver.maximize_window()
    
    # Найти первый продукт на главной странице
    first_product = driver.find_element(By.XPATH, '//div[@class="product-layout product-grid"]//a')
    first_product.click()
    
    # Проверка переключения скриншотов на странице продукта
    time.sleep(2)  # Подождать загрузку страницы
    screenshot_thumbnails = driver.find_elements(By.XPATH, '//div[@id="content"]//ul[@class="thumbnails"]/li')
    if len(screenshot_thumbnails) > 1:
        print("Скриншоты переключаются на странице продукта.")
    else:
        print("Скриншоты не переключаются на странице продукта.")
    
    # 2. Сменить валюту с доллара на евро и обратно
    # Найти элемент для смены валюты
    currency_dropdown = driver.find_element(By.XPATH, '//div[@class="btn-group"]/button')
    currency_dropdown.click()

    # Выбрать евро
    euro_currency = driver.find_element(By.XPATH, '//button[@name="EUR"]')
    euro_currency.click()

    # Подождать для проверки
    time.sleep(2)

    # Вернуться к доллару
    currency_dropdown.click()
    dollar_currency = driver.find_element(By.XPATH, '//button[@name="USD"]')
    dollar_currency.click()

    # 3. Перейти в категорию PC и проверить, что страница пуста
    menu_pc = driver.find_element(By.XPATH, '//ul[@class="nav navbar-nav"]/li/a[contains(text(), "PC")]')
    menu_pc.click()

    # Подождать загрузку страницы
    time.sleep(2)

    # Проверить, что страница пуста
    page_content = driver.find_element(By.XPATH, '//div[@id="content"]')
    if "There are no products to list in this category." in page_content.text:
        print("Страница категории PC пуста.")
    else:
        print("В категории PC есть продукты.")

    # 4. Перейти в регистрацию, заполнить все поля и нажать «зарегистрироваться»
    menu_register = driver.find_element(By.XPATH, '//ul[@class="nav navbar-nav"]/li/a[contains(text(), "Register")]')
    menu_register.click()

    # Заполнение формы регистрации
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

    # Согласие с политикой конфиденциальности
    agree_checkbox = driver.find_element(By.NAME, 'agree')
    agree_checkbox.click()

    # Нажать кнопку «зарегистрироваться»
    register_button = driver.find_element(By.XPATH, '//input[@value="Continue"]')
    register_button.click()

    # Подождать несколько секунд для завершения регистрации
    time.sleep(2)

    # 5. Написать поисковое слово в строке поиска и нажать кнопку поиска
    search_box = driver.find_element(By.NAME, 'search')
    search_box.send_keys('Laptop')  # Вводим слово "Laptop"
    search_box.send_keys(Keys.RETURN)  # Нажимаем Enter для поиска

    # Подождать результатов поиска
    time.sleep(3)

    # Проверить, что результаты поиска отобразились
    search_results = driver.find_element(By.XPATH, '//div[@id="content"]')
    if "No products were found" in search_results.text:
        print("Продукты не найдены.")
    else:
        print("Результаты поиска отображены.")

finally:
    # Закрыть браузер после выполнения всех шагов
    driver.quit()
