from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import main

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.w3schools.com/html/html_forms.asp")

search = driver.find_element_by_name("fname")
search = driver.find_element_by_name("lname")
search = driver.find_element_by_xpath("//*[@id='main']/div[3]/div/form/input[3]")
search.click()

