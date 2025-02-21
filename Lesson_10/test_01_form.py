import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.form_page import FormPage

@allure.title("Тест отправки формы")
@allure.description("Проверка отправки формы с различными данными")
@allure.feature("Form")
@allure.id("SKYPRO-1")
@allure.severity("Critical")
def test_form_submission():
    """
    Тестирование отправки формы и валидации ее полей.

    1. Открывает веб-страницу с формой.
    2. Заполняет форму с тестовыми данными.
    3. Отправляет форму.
    4. Проверяет правильность выделения полей формы после отправки (поле "Zip code" и другие поля).

    """
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    form_page = FormPage(driver)

    data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "zip-code": "",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }
    with allure.step("Открываем форму"):
        form_page.fill_form(data)
    with allure.step("Заполняем форму и отправляем"):
        form_page.submit_form()
    with allure.step("Проверяем"):
        form_page.wait_for_zip_code()
        alert_danger_color = "rgba(248, 215, 218, 1)"
        color_zip = form_page.get_zip_code_color()
        assert color_zip == alert_danger_color, f"Expected {alert_danger_color}, but got {color_zip}"

        alert_success_color = "rgba(209, 231, 221, 1)"
        fields = ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"]
        for field_name in fields:
            field_color = form_page.get_field_color(field_name)
            assert field_color == alert_success_color, f"Expected {alert_success_color} for {field_name}, but got {field_color}"

    driver.quit()
