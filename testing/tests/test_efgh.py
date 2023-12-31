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
        self.driver.find_element(By.CSS_SELECTOR, ".header > a").click()
        self.driver.find_element(By.CSS_SELECTOR, ".text-sm-center > .btn").click()
        self.driver.find_element(By.ID, "field-address1").click()
        self.driver.find_element(By.ID, "field-address1").send_keys("ul. Przykładowa")
        self.driver.find_element(By.ID, "field-postcode").click()
        self.driver.find_element(By.ID, "field-postcode").send_keys("80-123")
        self.driver.find_element(By.ID, "field-city").click()
        self.driver.find_element(By.ID, "field-city").send_keys("Gdańsk")
        self.driver.find_element(By.NAME, "confirm-addresses").click()
        self.driver.find_element(By.ID, "delivery_option_22").click()
        self.driver.find_element(By.ID, "delivery_message").click()
        self.driver.find_element(By.ID, "delivery_message").send_keys("Proszę ładnie zapakować.")
        self.driver.find_element(By.NAME, "confirmDeliveryOption").click()
        self.driver.find_element(By.ID, "payment-option-2").click()
        self.driver.find_element(By.ID, "conditions_to_approve[terms-and-conditions]").click()
        self.driver.find_element(By.CSS_SELECTOR, ".ps-shown-by-js > .btn").click()
