from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

for i in range (3):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("http://uitestingplayground.com/dynamicid")
    find_btn = driver.find_element(By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
    driver.quit()
