from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://www.facebook.com/')

assert 'Facebook' in driver.title

driver.find_element(By.ID,'email').send_keys("sonam@gmail.com")
driver.find_element(By.ID,'pass').send_keys("1234567890")
driver.find_element(By.NAME,'login').click() 
time.sleep(5)

driver.quit()
