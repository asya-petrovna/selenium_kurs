from unittest import TestCase

from drivers import DriverFactory
from steps_for_widget import UsedSteps


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

        driver.find_element_by_css_selector("input#uclw_form_height").send_keys('165')
        driver.find_element_by_css_selector("input#uclw_form_weight").send_keys('60')
        self.steps.find_and_click_on_element("button#uclw_save_info_button")

        driver.find_element_by_css_selector().click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[contains(.,"Ihre Bauchform")]')))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "li.uclw_item.uclw_key_1")))
        time.sleep(1)
        driver.find_element_by_css_selector('li.uclw_item.uclw_key_1').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[contains(.,"Ihre Hüftform")]')))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "li.uclw_item.uclw_key_1")))
        time.sleep(1)
        driver.find_element_by_css_selector('span#uclw_item_shape_1').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[contains(.,"hinzufügen")]')))
        time.sleep(2)
        driver.find_element_by_css_selector('.uclw_section.uclw_left .uclw_item.uclw_key_2').click()
        driver.find_element_by_css_selector('.uclw_section.uclw_right .uclw_item.uclw_key_2').click()
        driver.find_element_by_css_selector('button.uclw_button.uclw_submit_form_button').click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.uclw_input_text')))
        driver.find_element_by_css_selector('input.uclw_input_text').send_keys('30')
        driver.find_element_by_css_selector('button.uclw_button.uclw_submit_form_button').click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.uclw_field_label')))

        Keys.TAB()
        Keys.ARROW_LEFT
        time.sleep(2)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[contains(.,"Etwas enger")]')))
        time.sleep(2)
        driver.find_element_by_css_selector('button.uclw_button.uclw_submit_form_button').click()
