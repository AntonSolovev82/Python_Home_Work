from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


driver.get("http://the-internet.herokuapp.com/entry_ad")

sleep(3)

close_btn = driver.find_element(By.XPATH, "//div[@class='modal-footer']/p")

close_btn.click()

sleep(3)

driver.quit()
