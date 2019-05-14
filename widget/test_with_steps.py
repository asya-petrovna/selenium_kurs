import time
from unittest import TestCase, TestLoader, TestSuite

from HtmlTestRunner import HTMLTestRunner
from parameterized import parameterized
from selenium.webdriver.common.by import By

from drivers import DriverFactory
from widget.steps import UsedSteps


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
        self.steps.wait_until_element_presence(By.CSS_SELECTOR, 'div.uclw_fit_indicators_right')
        time.sleep(2)
        self.steps.find_and_click_on_element('div.uclw_fit_indicators_right')
        self.assertEqual(driver.find_element_by_css_selector("div.uclw_fit_fit span").get_attribute('textContent'),
                         'Etwas lockerer')
        time.sleep(3)
        driver.find_element_by_css_selector('button.uclw_button.uclw_submit_form_button').click()
        time.sleep(3)
        self.assertEqual(driver.find_element_by_css_selector("#aria_uclw_headline").get_attribute('textContent'),
                         'Ihre beste Größe')


if __name__ == '__main__':
    # opening file streams
    # outfile = open("test-report.html", "w")
    # with open('test-report.html', 'w') as outfile:

    # running test with report. more on that: https://github.com/oldani/HtmlTestRunner#usage
    runner = HTMLTestRunner(report_title='Test Report', report_name='TestReport')
    runner.run(TestLoader().loadTestsFromTestCase(TestsUsingWidgetForDifferentSites))
