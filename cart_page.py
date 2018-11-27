from selenium.webdriver.support import expected_conditions as EC

from basic_page import BasicPage


class CartPage(BasicPage):

    def del_item_from_cart(self):
        old_row = self.driver.find_elements_by_css_selector('#box-checkout-summary tr')[1]
        self.driver.find_element_by_css_selector('button[name = "remove_cart_item"]').click()
        self.wait.until(EC.staleness_of(old_row))

    def is_cart_empty(self):
        return not self.is_element_present('#box-checkout-summary')
