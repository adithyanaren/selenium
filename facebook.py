from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import main

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.facebook.com/")

Uname = driver.find_element_by_name("email")
Uname.send_keys("adithya.ak6@gmail.com")
Pass = driver.find_element_by_name("pass")
Pass.send_keys("Optimus16#")
click = driver.find_element_by_name("login")
click.click()
story = driver.find_element_by_xpath("//*[@id='facebook']/body")
story.click()
driver.open()


