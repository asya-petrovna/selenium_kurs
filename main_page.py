from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from basic_page import BasicPage


class MainShopPage(BasicPage):

    def login(self, email, password):
        self.driver.get('http://localhost:8080/litecart/en/')
        self.driver.find_element_by_css_selector("input[name = 'email']").clear()
        self.driver.find_element_by_css_selector("input[name = 'email']").send_keys(email, Keys.TAB)
        self.driver.find_element_by_css_selector("input[name = 'password']").clear()
        self.driver.find_element_by_css_selector("input[name = 'password']").send_keys(password, Keys.TAB)
        self.driver.find_element_by_css_selector("button[name = 'login']").click()
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'list-vertical')))

    def open(self):
        return self.driver.get('http://localhost:8080/litecart/en/')

    def choose_first_good(self):
        self.driver.find_elements_by_css_selector("#box-most-popular a")[0].click()
        self.wait.until(EC.presence_of_element_located((By.NAME, 'add_cart_product')))

    def go_to_checkout(self):
        self.driver.find_element_by_xpath(f"//*[contains(text(), 'Checkout')]").click()

    def get_cart_counter(self):
        counter = self.driver.find_element_by_css_selector("#cart-wrapper .quantity")
        return int(counter.get_attribute("textContent"))
