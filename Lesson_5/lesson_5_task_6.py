from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")

sleep(3)
# как было
#username_field = driver.find_element(By.ID, "username")
#username_field.send_keys("tomsmith")
# и стало с использованием одной переменной
driver.find_element(By.ID, "username").send_keys("tomsmith")
# и
#password_field = driver.find_element(By.ID, "password")
#password_field.send_keys("SuperSecretPassword!")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_btn.click()

sleep(3)

driver.quit()
