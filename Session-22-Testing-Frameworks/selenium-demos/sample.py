from selenium import webdriver
from selenium.webdriver.common.by import By

# open chrome browser
driver = webdriver.Chrome()

# open below web page
driver.get('https://selenium.dev/documentation')
# check the title and assert
assert 'Selenium' in driver.title
# access element
elem = driver.find_element(By.ID, 'm-documentationwebdriver')
elem.click() # click on that elemen
# check title in that as well
assert 'WebDriver' in driver.title
