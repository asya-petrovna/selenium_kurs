from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class UsedSteps:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_and_click_on_element(self, selector):
        self.driver.find_element_by_css_selector(selector).click()

    def wait_until_element_presence(self, method, selector):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((method, selector)))

    def find_and_fill_input(self, selector, text):
        self.driver.find_element_by_css_selector(selector).send_keys(text)
