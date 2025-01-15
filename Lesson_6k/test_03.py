from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"
FIRST_NAME = "Anton"
LAST_NAME = "Solovev"
POSTAL_CODE = "196066"
EXPECTED_TOTAL = "Total: $58.29"


def login(driver):
    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()


def add_items_to_cart(driver):
    items = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie"
    ]

    for item in items:
        driver.find_element(By.ID, item).click()


def checkout(driver):
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys(FIRST_NAME)
    driver.find_element(By.ID, "last-name").send_keys(LAST_NAME)
    driver.find_element(By.ID, "postal-code").send_keys(POSTAL_CODE)

    driver.find_element(By.ID, "continue").click()


def verify_total(driver):
    total_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    total_value = total_element.text
    assert total_value == EXPECTED_TOTAL, f"Expected total to be {EXPECTED_TOTAL}, but got {total_value}"


def test_shop():
    try:

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get(URL)

        login(driver)

        add_items_to_cart(driver)

        checkout(driver)

        verify_total(driver)

    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        driver.quit()


test_shop()
