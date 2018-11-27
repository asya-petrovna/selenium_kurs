from basic_page import BasicPage


class GoodsPage(BasicPage):

    def add_good_to_cart(self):
        if self.is_element_present('select'):
            self.find_select().select_by_visible_text('Small')
        self.driver.find_element_by_css_selector('button[name = "add_cart_product"]').click()
        self.close_alert_if_present()

    def check_counter_after_adding_good(self):
        self.driver.refresh()
        return self.driver.find_element_by_css_selector("#cart-wrapper .quantity").get_attribute(
            "textContent")

    def go_to_checkout(self):
        return self.driver.find_element_by_xpath(f"//*[contains(text(), 'Checkout')]").click()
