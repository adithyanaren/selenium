from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.youtube.com")

search = driver.find_element_by_link_text("Search")
search.send_keys("adhithya narendran")
