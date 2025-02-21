import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.calculator_page import CalculatorPage

@allure.title("Тест калькулятора")
@allure.description("Проверка работы калькулятора")
@allure.feature("Calculator")
@allure.id("SKYPRO-2")
@allure.severity("Critical")
def test_02_calc():
    """
        Тест для калькулятора, проверяющий выполнение операций с задержкой.
        Щаги
        1 Вход на страницу калькулятора
        2 Ввод данных(нажатие на кнопки)
        3 Ожидание ответа
        4 Проверка ответа
    """
    with allure.step("Вход на страницу калькулятора"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        calculator_page = CalculatorPage(driver)

    with allure.step("Нажимаем кнопки 7, +, 8 и ="):
        calculator_page.set_delay("45")
        calculator_page.click_button()
    with allure.step("Проверка ответа"):
        result = calculator_page.get_result("15")
        assert result == "15"

        driver.quit()
