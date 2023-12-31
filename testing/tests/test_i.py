# Generated by Selenium IDE
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

# FIXME
class Test:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test(self):
        self.driver.get("https://prestashop:8443/index.php")
        self.driver.maximize_window()
        self.driver.find_element(By.CSS_SELECTOR, ".account > .hidden-sm-down").click()
        self.driver.find_element(By.CSS_SELECTOR, "#history-link .material-icons").click()
        self.driver.find_element(By.LINK_TEXT, "Szczegóły").click()
        self.driver.find_element(By.NAME, "id_product").click()
        dropdown = self.driver.find_element(By.NAME, "id_product")
        dropdown.find_element(By.XPATH, "//option[. = 'Mysz Asus TUF Gaming M3']").click()
        self.driver.find_element(By.NAME, "msgText").click()
        self.driver.find_element(By.NAME, "msgText").send_keys("Niech fajnie klika.")
        self.driver.find_element(By.NAME, "submitMessage").click()
