# Generated by Selenium IDE

import pytest
import time
import json
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Test:
    def setup_method(self):
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--allow-insecure-localhost')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.vars = {}

    def teardown_method(self):
        pass
        # self.driver.quit()

    def test(self):
        self.driver.get("https://prestashop:18466/index.php")
        self.driver.maximize_window()
        element = self.driver.find_element(By.LINK_TEXT, "Laptopy")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.LINK_TEXT, "Torby do laptopów").click()
        self.driver.find_element(By.CSS_SELECTOR, ".thumbnail > img").click()
        self.driver.find_element(By.CSS_SELECTOR, ".touchspin-up").click()
        self.driver.find_element(By.CSS_SELECTOR, ".touchspin-up").click()
        self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary").click()
        element = self.driver.find_element(By.LINK_TEXT, "Podzespoły PC")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.LINK_TEXT, "Dyski SSD").click()
        self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(1) img").click()
        self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary").click()
        self.driver.find_element(By.CSS_SELECTOR, "ol > li:nth-child(4) span").click()
        self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(2) img").click()
        self.driver.find_element(By.CSS_SELECTOR, ".touchspin-up").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary > .material-icons").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary").click()
        self.driver.find_element(By.CSS_SELECTOR, "ol > li:nth-child(4) span").click()
        self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(3) img").click()
        self.driver.find_element(By.CSS_SELECTOR, ".bootstrap-touchspin-up").click()
        self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary").click()
        self.driver.find_element(By.CSS_SELECTOR, "ol > li:nth-child(4) span").click()
        self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(4) img").click()
        self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary").click()
        self.driver.find_element(By.CSS_SELECTOR, "ol > li:nth-child(4) span").click()
        self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(5) img").click()
        self.driver.find_element(By.CSS_SELECTOR, "ol > li:nth-child(4) span").click()
        self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(6) img").click()
        self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".bootstrap-touchspin-down")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary").click()
        self.driver.find_element(By.CSS_SELECTOR, "ol > li:nth-child(4) span").click()
        self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(7) img").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary > .material-icons").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary").click()
        self.driver.find_element(By.CSS_SELECTOR, "ol > li:nth-child(4) span").click()
        self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(8) img").click()
        self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".bootstrap-touchspin-down")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary").click()
        self.driver.find_element(By.CSS_SELECTOR, "ol > li:nth-child(4) span").click()
        self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(9) img").click()
        self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary").click()
        self.driver.find_element(By.CSS_SELECTOR, "ol > li:nth-child(4) span").click()
        self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(10) img").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary > .material-icons").click()
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary").click()
        self.driver.find_element(By.CSS_SELECTOR, ".header .hidden-sm-down").click()

        #### TEST 2 ####

        self.driver.find_element(By.NAME, "s").click()
        self.driver.find_element(By.NAME, "s").send_keys("mysz")
        self.driver.find_element(By.NAME, "s").send_keys(Keys.ENTER)
        product_list = self.driver.find_element(By.CSS_SELECTOR, ".products")
        children = product_list.find_elements(By.CSS_SELECTOR, ".js-product")
        children[random.randint(0, len(children) - 1)].click()
        self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-primary").click()

        #### TEST 3 ####

        self.driver.find_element(By.CSS_SELECTOR, ".cart-item:nth-child(3) .col-md-2 .material-icons").click()
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.CSS_SELECTOR, ".cart-item:nth-child(2) .col-md-2 .material-icons").click()
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.CSS_SELECTOR, ".cart-item:nth-child(1) .col-md-2 .material-icons").click()
        self.driver.implicitly_wait(30)

        #### TEST 4 ####

        self.driver.find_element(By.CSS_SELECTOR, "a > .hidden-sm-down").click()
        self.driver.find_element(By.LINK_TEXT, "Nie masz konta? Załóż je tutaj").click()
        self.driver.find_element(By.ID, "field-id_gender-1").click()
        self.driver.find_element(By.ID, "field-firstname").click()
        self.driver.find_element(By.ID, "field-firstname").send_keys("Jan")
        self.driver.find_element(By.ID, "field-lastname").send_keys("Kowalski")
        self.driver.find_element(By.ID, "field-email").send_keys(f"szybkipingwin+{random.randint(0, 10000)}@gmail.com")
        self.driver.find_element(By.ID, "field-password").send_keys("haslo123")
        self.driver.find_element(By.ID, "field-birthday").click()
        self.driver.find_element(By.ID, "field-birthday").send_keys("1970-05-31")
        self.driver.find_element(By.NAME, "optin").click()
        self.driver.find_element(By.NAME, "customer_privacy").click()
        self.driver.find_element(By.NAME, "newsletter").click()
        self.driver.find_element(By.NAME, "psgdpr").click()
        self.driver.find_element(By.CSS_SELECTOR, ".form-control-submit").click()
        self.driver.find_element(By.CSS_SELECTOR, ".account > .hidden-sm-down").click()

        #### THE REST ####

        self.driver.find_element(By.CSS_SELECTOR, ".header-options:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".text-sm-center > .btn").click()
        self.driver.find_element(By.ID, "field-alias").click()
        self.driver.find_element(By.ID, "field-alias").send_keys("Lol")
        self.driver.find_element(By.ID, "field-company").click()
        self.driver.find_element(By.ID, "field-company").send_keys("jakaś")
        self.driver.find_element(By.ID, "field-vat_number").click()
        self.driver.find_element(By.ID, "field-vat_number").click()
        self.driver.find_element(By.ID, "field-vat_number").send_keys("123123333333")
        self.driver.find_element(By.ID, "field-address1").click()
        self.driver.find_element(By.ID, "field-address1").send_keys("ul. Przykładowa")
        self.driver.find_element(By.ID, "field-address2").click()
        self.driver.find_element(By.ID, "field-address2").send_keys("12/3")
        self.driver.find_element(By.ID, "field-postcode").click()
        self.driver.find_element(By.ID, "field-postcode").send_keys("80-123")
        self.driver.find_element(By.ID, "field-city").click()
        self.driver.find_element(By.ID, "field-city").send_keys("Gdańsk")
        self.driver.find_element(By.ID, "field-id_country").click()
        self.driver.find_element(By.ID, "field-phone").click()
        self.driver.find_element(By.ID, "field-phone").send_keys("123456789")
        self.driver.find_element(By.NAME, "confirm-addresses").click()
        self.driver.find_element(By.ID, "delivery_option_32").click()
        self.driver.find_element(By.ID, "delivery_message").click()
        self.driver.find_element(By.ID, "delivery_message").send_keys("Proszę nie rozbić.")
        self.driver.find_element(By.NAME, "confirmDeliveryOption").click()
        self.driver.find_element(By.ID, "payment-option-2").click()
        self.driver.find_element(By.ID, "conditions_to_approve[terms-and-conditions]").click()

        ### Finalize order ###

        self.driver.find_element(By.CSS_SELECTOR, ".ps-shown-by-js > .btn").click()
        self.driver.find_element(By.CSS_SELECTOR, ".account > .hidden-sm-down").click()
        self.driver.find_element(By.CSS_SELECTOR, "#order-slips-link .material-icons").click()
        self.driver.find_element(By.CSS_SELECTOR, "ol > li:nth-child(2) span").click()
        self.driver.find_element(By.CSS_SELECTOR, "#history-link .material-icons").click()
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) .material-icons").click()

