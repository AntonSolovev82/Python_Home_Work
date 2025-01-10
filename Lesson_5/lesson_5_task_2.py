from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

for i in range (3):

    driver.get("http://uitestingplayground.com/dynamicid")
    sleep(5)
    find_btn = driver.find_element(By.XPATH, '//button[text()="Button with Dynamic ID"]').click()
    sleep(5)

driver.quit()
