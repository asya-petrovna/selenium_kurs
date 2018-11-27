from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class BasicPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 3)

    def is_element_present(self, selector):
        try:
            self.driver.find_element_by_css_selector(selector)
            return True
        except NoSuchElementException:
            return False

    def close_alert_if_present(self):
        try:
            self.wait.until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            pass

    def find_select(self, css_selector='select'):
        return Select(self.driver.find_element_by_css_selector(css_selector))

    def refresh(self):
        self.driver.refresh()

    def back(self):
        self.driver.back()
