from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Константы
URL = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
ALERT_DANGER_COLOR = "rgba(248, 215, 218, 1)"
ALERT_SUCCESS_COLOR = "rgba(209, 231, 221, 1)"
FIELDS = {
    "first-name": "Иван",
    "last-name": "Петров",
    "address": "Ленина, 55-3",
    "e-mail": "test@skypro.com",
    "phone": "+7985899998787",
    "city": "Москва",
    "country": "Россия",
    "job-position": "QA",
    "company": "SkyPro"
}

def fill_form(driver):
    for field_name, value in FIELDS.items():
        driver.find_element(By.NAME, field_name).send_keys(value)

def check_field_color(driver, field_name, expected_color):
    field = driver.find_element(By.CSS_SELECTOR, f"[id='{field_name}']")
    field_color = field.value_of_css_property("background-color")
    assert field_color == expected_color, f"Expected {expected_color} for {field_name}, but got {field_color}"

def test_01_form():
    try:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get(URL)

        fill_form(driver)

        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        ).click()

        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, "zip-code"))
        )

        zip_code = driver.find_element(By.ID, "zip-code")
        color_zip = zip_code.value_of_css_property("background-color")
        assert color_zip == ALERT_DANGER_COLOR, f"Expected {ALERT_DANGER_COLOR}, but got {color_zip}"

        for field_name in FIELDS.keys():
            check_field_color(driver, field_name, ALERT_SUCCESS_COLOR)

    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        driver.quit()

# Запуск теста
test_01_form()
