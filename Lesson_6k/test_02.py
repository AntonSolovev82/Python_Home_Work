from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def setup_driver():
    return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def set_delay(driver, delay):
    delay_input = driver.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys(str(delay))


def perform_calculation(driver, num1, operator, num2):
    driver.find_element(By.XPATH, f"//span[text()='{num1}']").click()
    driver.find_element(By.XPATH, f"//span[text()='{operator}']").click()
    driver.find_element(By.XPATH, f"//span[text()='{num2}']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()


def get_result(driver):
    """Получение результата вычисления."""
    wait = WebDriverWait(driver, 50)
    return wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))


def test_calc(delay=45, num1=7, operator='+', num2=8):
    try:
        driver = setup_driver()
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        set_delay(driver, delay)
        perform_calculation(driver, num1, operator, num2)

        result = get_result(driver)
        assert result, f"Результат не равен 15, фактический результат: {result}"

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_calc()
