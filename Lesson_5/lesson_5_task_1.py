from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver: WebDriver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

for i in range(5):
    driver.find_element(By.XPATH, '//button[text()="Add Element"]').click()
sleep(5)

delete_btn = driver.find_elements(By.XPATH, '//button[text()="Delete"]')
print("Размер списка Delete:", len(delete_btn))

sleep(5)

driver.quit()
