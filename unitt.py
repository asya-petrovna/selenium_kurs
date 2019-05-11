# -*- coding: utf-8 -*-

import os
import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestsForTnfWidget(unittest.TestCase):

    def setUp(self):
        home_dir = os.getenv('HOME')
        chromedriver_location = os.path.join(home_dir, 'bin', 'chromedriver')
        self.chrome = webdriver.Chrome(chromedriver_location)

    def test_widget(self):
        chrome = self.chrome
        chrome.get("https://www.thenorthface.de/shop/de/tnf-de/damen-jacken/damen-fanorak-2-0-jacke-3sv8?variationId=L48")
        chrome.find_element_by_css_selector('span.close').click()
        WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.fitanalytics__button-text')))
        chrome.find_element_by_css_selector('.fitanalytics__button-text').click()
        WebDriverWait(chrome, 4).until(EC.presence_of_element_located((By.XPATH, '//*[contains(.,"Ihre Angaben")]')))
        chrome.find_element_by_css_selector("input#uclw_form_height").send_keys('165')
        chrome.find_element_by_css_selector("input#uclw_form_weight").send_keys('60')
        chrome.find_element_by_css_selector("button#uclw_save_info_button").click()
        WebDriverWait(chrome, 4).until(EC.presence_of_element_located((By.XPATH, '//*[contains(.,"Ihre Bauchform")]')))
        chrome.find_element_by_css_selector('li.uclw_item.uclw_key_1').click()
        WebDriverWait(chrome, 4).until(EC.presence_of_element_located((By.XPATH, '//*[contains(.,"Ihre Hüftform")]')))
        chrome.find_element_by_css_selector('span#uclw_item_shape_1').click()
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()