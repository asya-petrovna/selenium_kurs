from drivers import drivers
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MainShopPage:

    def __init__(self, driver):
        self.driver = drivers.create_chrome_driver()
        self.wait = WebDriverWait(driver, 10)

    def login_as_customer(self):
        self.driver.get('http://localhost:8080/litecart/en/')
        self.driver.find_element_by_css_selector("input[name = 'email']").clear()
        self.driver.find_element_by_css_selector("input[name = 'email']").send_keys("asya.gush@gmail.com", Keys.TAB)
        self.driver.find_element_by_css_selector("input[name = 'password']").clear()
        self.driver.find_element_by_css_selector("input[name = 'password']").send_keys("123456", Keys.TAB)
        self.driver.find_element_by_css_selector("button[name = 'login']").click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'list-vertical')))

    def open_main_page(self):
        return self.driver.get('http://localhost:8080/litecart/en/')

    def choose_first_good(self):
        return self.driver.find_elements_by_css_selector("#box-most-popular a")[0].click()

    def go_to_checkout(self):
        return self.driver.find_element_by_xpath(f"//*[contains(text(), 'Checkout')]").click()

    def check_counter_before_adding_good(self):
        pre_quantity = self.driver.find_element_by_css_selector("#cart-wrapper .quantity").get_attribute("textContent")
        return pre_quantity

    def check_counter_after_adding_good(self):
        driver.refresh()
        post_quantity = self.driver.find_element_by_css_selector("#cart-wrapper .quantity").get_attribute(
            "textContent")
        return post_quantity

    def check_cart_is_empty(self):
        assert driver.find_element_by_css_selector("#cart-wrapper .quantity").get_attribute(
            "textContent") == '0'
