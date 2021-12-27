from selenium import webdriver
driver = webdriver.Firefox(executable_path='C:\Users\adith\PycharmProjects\pythonProject2\.geckodriver.exe')
driver.get("https://www.facebook.com/")
print(driver.title)
driver.close()
