from steps_for_widget import UsedSteps


class Tests_using_wodget_for_different_sites(unittest.TestCase, UsedSteps):

    @parameterized.expand([
        'https://www.thenorthface.de/shop/de/tnf-de/damen-jacken/damen-fanorak-2-0-jacke-3sv8?variationId=L48'
    ])
    def test_parameterized_for_classic_customization(self, PDP):
        chrome = self.chrome
        self.setUp()
        chrome.get(PDP)
        self.find_and_click_on_element('span.close')

        chrome.find_element_by_css_selector().click()
        WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.fitanalytics__button-text')))
        chrome.find_element_by_css_selector('.fitanalytics__button-text').click()
        WebDriverWait(chrome, 4).until(EC.presence_of_element_located((By.XPATH, '//*[contains(.,"Ihre Angaben")]')))
        chrome.find_element_by_css_selector("input#uclw_form_height").send_keys('165')
        chrome.find_element_by_css_selector("input#uclw_form_weight").send_keys('60')
        chrome.find_element_by_css_selector("button#uclw_save_info_button").click()
        WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.XPATH, '//*[contains(.,"Ihre Bauchform")]')))
        WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "li.uclw_item.uclw_key_1")))
        time.sleep(1)
        chrome.find_element_by_css_selector('li.uclw_item.uclw_key_1').click()
        WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.XPATH, '//*[contains(.,"Ihre Hüftform")]')))
        WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "li.uclw_item.uclw_key_1")))
        time.sleep(1)
        chrome.find_element_by_css_selector('span#uclw_item_shape_1').click()
        WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.XPATH, '//*[contains(.,"hinzufügen")]')))
        time.sleep(2)
        chrome.find_element_by_css_selector('.uclw_section.uclw_left .uclw_item.uclw_key_2').click()
        chrome.find_element_by_css_selector('.uclw_section.uclw_right .uclw_item.uclw_key_2').click()
        chrome.find_element_by_css_selector('button.uclw_button.uclw_submit_form_button').click()
        WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.uclw_input_text')))
        chrome.find_element_by_css_selector('input.uclw_input_text').send_keys('30')
        chrome.find_element_by_css_selector('button.uclw_button.uclw_submit_form_button').click()
        time.sleep(2)
        WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.uclw_field_label')))

        Keys.TAB()
        Keys.ARROW_LEFT
        time.sleep(2)
        WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.XPATH, '//*[contains(.,"Etwas enger")]')))
        time.sleep(2)
        chrome.find_element_by_css_selector('button.uclw_button.uclw_submit_form_button').click()
