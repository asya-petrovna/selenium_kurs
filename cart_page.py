from drivers import drivers
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from steps import is_element_present


class CartPage():
    def __init__(self, driver):
        self.driver = drivers.create_chrome_driver()
        self.wait = WebDriverWait(driver, 10)

    def del_item_from_cart(self):
        old_row = self.driver.find_elements_by_css_selector('#box-checkout-summary tr')[1]
        self.driver.find_element_by_css_selector('button[name = "remove_cart_item"]').click()
        WebDriverWait(self.driver, 3).until(EC.staleness_of(old_row))

    def cart_not_empty(self):
        is_element_present(self.driver, '#box-checkout-summary')
        return True
