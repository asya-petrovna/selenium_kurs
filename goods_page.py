from drivers import drivers
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from steps import is_element_present
from steps import close_alert_if__present
from selenium.webdriver.support.ui import Select


class PageOfGood():
    def __init__(self, driver):
        self.driver = drivers.create_chrome_driver()
        self.wait = WebDriverWait(driver, 10)

    def add_good_to_cart(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.NAME, 'add_cart_product')))
        if is_element_present(self.driver, 'select'):
            select = Select(self.driver.find_element_by_css_selector('select'))
            select.select_by_visible_text('Small')
        self.driver.find_element_by_css_selector('button[name = "add_cart_product"]').click()
        close_alert_if__present(self.driver)

    def check_counter_after_adding_good(self):
        driver.refresh()
        post_quantity = self.driver.find_element_by_css_selector("#cart-wrapper .quantity").get_attribute(
            "textContent")
        return post_quantity

    def go_to_checkout(self):
        return self.driver.find_element_by_xpath(f"//*[contains(text(), 'Checkout')]").click()
