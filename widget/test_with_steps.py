from unittest import TestCase
import time
from drivers import DriverFactory
from widget.steps import UsedSteps
from parameterized import parameterized
from selenium.webdriver.common.by import By


class TestsUsingWidgetForDifferentSites(TestCase):

    def setUp(self):
        self.driver = DriverFactory().create_chrome_driver()
        self.steps = UsedSteps(
            self.driver)  # initializirovala stepi iz UsedSteps, teper' oni rabotaut c ukazannim driverom

    @parameterized.expand([
        'https://www.thenorthface.de/shop/de/tnf-de/damen-jacken/damen-fanorak-2-0-jacke-3sv8?variationId=L48'
    ])
    def test_parameterized_for_classic_customization(self, pdp):
        driver = self.driver
        self.driver.get(pdp)
        self.steps.find_and_click_on_element('span.close')
        self.steps.wait_until_element_presence(By.CSS_SELECTOR, '.fitanalytics__button-text')
        self.steps.find_and_click_on_element('.fitanalytics__button-text')
        self.steps.wait_until_element_presence(By.XPATH, '//*[contains(.,"Ihre Angaben")]')
        self.steps.find_and_fill_input("input#uclw_form_height", '165')
        self.steps.find_and_fill_input("input#uclw_form_weight", '60')
        self.steps.find_and_click_on_element("button#uclw_save_info_button")
        self.steps.wait_until_element_presence(By.XPATH, '//*[contains(.,"Ihre Bauchform")]')
        self.steps.wait_until_element_presence(By.CSS_SELECTOR, "li.uclw_item.uclw_key_1")
        time.sleep(1)
        self.steps.find_and_click_on_element('li.uclw_item.uclw_key_1')
        self.steps.wait_until_element_presence(By.XPATH, '//*[contains(.,"Ihre Hüftform")]')
        self.steps.wait_until_element_presence(By.CSS_SELECTOR, "li.uclw_item.uclw_key_1")
        time.sleep(1)
        self.steps.find_and_click_on_element('span#uclw_item_shape_1')
        self.steps.wait_until_element_presence(By.XPATH, '//*[contains(.,"hinzufügen")]')
        time.sleep(2)
        self.steps.find_and_click_on_element('.uclw_section.uclw_left .uclw_item.uclw_key_2')
        self.steps.find_and_click_on_element('.uclw_section.uclw_right .uclw_item.uclw_key_2')
        self.steps.find_and_click_on_element('button.uclw_button.uclw_submit_form_button')
        self.steps.wait_until_element_presence(By.CSS_SELECTOR, 'input.uclw_input_text')
        self.steps.find_and_fill_input('input.uclw_input_text', '30')
        self.steps.find_and_click_on_element('button.uclw_button.uclw_submit_form_button')
        time.sleep(2)
        self.steps.wait_until_element_presence(By.CSS_SELECTOR, 'span.uclw_field_label')
        time.sleep(2)
        #        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[contains(.,"Etwas enger")]')))

        driver.find_element_by_css_selector('button.uclw_button.uclw_submit_form_button').click()
