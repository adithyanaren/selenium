from selenium import webdriver
driver = webdriver.Chrome('./Chromedriver')
driver.get("https://www.instagram.com")
print(driver.title)
driver.open()