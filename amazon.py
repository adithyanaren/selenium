
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3F%26ext_vrnc%3Dhi%26tag%3Dgooghydrabk1-21%26ref%3Dnav_signin%26adgrpid%3D58355126069%26hvpone%3D%26hvptwo%3D%26hvadid%3D486458755421%26hvpos%3D%26hvnetw%3Dg%26hvrand%3D7419216462273469183%26hvqmt%3De%26hvdev%3Dc%26hvdvcmdl%3D%26hvlocint%3D%26hvlocphy%3D9061896%26hvtargid%3Dkwd-10573980%26hydadcr%3D14453_2154373%26gclid%3DCjwKCAiAn5uOBhADEiwA_pZwcOCLs7QR_YVgY07k7595QXLPIju2ZQOMtAA5T4gey3TGcTW4VaAUzxoCFksQAvD_BwE&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
login = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[1]/input[1]")
login.send_keys("adithya.ak6@gmail.com")

select = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[2]/span/span/input")
select.click()

password = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div[1]/div/div/form/div/div[1]/input")
password.send_keys("Optimus16#")

signin = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div[1]/div/div/form/div/div[2]/span/span/input")
signin.click()






