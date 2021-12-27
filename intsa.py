import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestTest1():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_instalogintest(self):
        self.driver.get("https://www.instagram.com/")
        self.driver.set_window_size(1552, 832)
        self.driver.execute_script("window.scrollTo(0,511.20001220703125)")
        self.driver.find_element(By.LINK_TEXT, "adithya.naren").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.execute_script("window.scrollTo(0,2016)")
        self.driver.find_element(By.LINK_TEXT, "Edit Profile").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.close()
