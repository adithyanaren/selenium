from selenium import webdriver
from selenium.webdriver.common.keys import keys
driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.google.com/")
print(driver.title)
driver.open()