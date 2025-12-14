from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# open chrome browser
driver = webdriver.Chrome()

# open below web page
driver.get('https://www.google.com/')
# check the title and assert
assert 'Google' in driver.title
# find search box
elem = driver.find_element(By.NAME, 'q')
elem.send_keys("selenium")
elem.send_keys(Keys.ENTER)

time.sleep(3)
print("Page Title ", driver.title)

driver.close()
