import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.shopping_cart_page import ShopPage

@allure.title("Тест корзины покупок")
@allure.description("Проверка работы корзины покупок")
@allure.feature("Shopping cart")
@allure.id("SKYPRO-3")
@allure.severity("Blocker")
def test_03_shop():
    """
    Тест на суммы стоимости товаров в корзине
    Шаги:
    1 Вход в магазин
    2 Заполняем форму
    3 Выбираем товары
    4 Заходим в корзину
    5 Проверяем результат
    :return:
    """
    with allure.step("Вход в магазин"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        shop_page = ShopPage(driver)
    with allure.step("Заполняем форму"):
        shop_page.fill_form("standard_user", "secret_sauce")
    with allure.step("Выбираем товары"):
        shop_page.add_products()
    with allure.step("Заходим в корзину"):
        shop_page.shopping_cart()
    with allure.step("Проверяем результат"):
        shop_page.checkout()
        shop_page.your_information("Anton", "Solovev", "196066")
        total_value = shop_page.total()

    assert total_value == "Total: $58.29"
    driver.quit()
