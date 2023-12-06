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

class TestAAdding10productswithvaryingquantities():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_aAdding10productswithvaryingquantities(self):
    self.driver.get("https://prestashop:8443/index.php")
    self.driver.set_window_size(1936, 1056)
    self.driver.find_element(By.LINK_TEXT, "Torby do laptopów").click()
    self.driver.find_element(By.CSS_SELECTOR, ".thumbnail > img").click()
    self.driver.find_element(By.CSS_SELECTOR, ".touchspin-up").click()
    self.driver.find_element(By.CSS_SELECTOR, ".touchspin-up").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".touchspin-up")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
    self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary").click()
    self.driver.find_element(By.CSS_SELECTOR, "#category-16 > .dropdown-item").click()
    self.driver.find_element(By.LINK_TEXT, "Dyski HDD").click()
    self.driver.find_element(By.CSS_SELECTOR, "#top_sub_menu_70623 > .top-menu").click()
    self.driver.find_element(By.LINK_TEXT, "Dyski SSD").click()
    element = self.driver.find_element(By.LINK_TEXT, "Dyski SSD")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(1) img").click()
    self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
    self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary").click()
    self.driver.find_element(By.LINK_TEXT, "Dyski SSD").click()
    self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(3) img").click()
    self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
    self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary").click()
    self.driver.find_element(By.LINK_TEXT, "Dyski SSD").click()
    self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(2) img").click()
    self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
    self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary").click()
    self.driver.find_element(By.LINK_TEXT, "Dyski SSD").click()
    self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(4) img").click()
    self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".touchspin-down")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary").click()
    self.driver.find_element(By.ID, "wrapper").click()
    self.driver.find_element(By.LINK_TEXT, "Dyski SSD").click()
    self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(5) img").click()
    self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
    self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary").click()
    self.driver.find_element(By.LINK_TEXT, "Dyski SSD").click()
    self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(6) img").click()
    self.driver.find_element(By.CSS_SELECTOR, ".product-quantity").click()
    self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
    self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary").click()
    self.driver.find_element(By.LINK_TEXT, "Dyski SSD").click()
    self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(7) img").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary > .material-icons").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary").click()
    self.driver.find_element(By.LINK_TEXT, "Dyski SSD").click()
    self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(8) img").click()
    self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
    self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary").click()
    self.driver.find_element(By.LINK_TEXT, "Dyski SSD").click()
    self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(9) img").click()
    self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary").click()
  
