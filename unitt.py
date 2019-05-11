# -*- coding: utf-8 -*-

import os
import unittest
from selenium import webdriver
import time

class TestsForTnfWidget(unittest.TestCase):

    def setUp(self):
        home_dir = os.getenv('HOME')
        chromedriver_location = os.path.join(home_dir, 'bin', 'chromedriver')
        self.chrome = webdriver.Chrome(chromedriver_location)

    def test_widget(self):
        chrome = self.chrome
        chrome.get("https://www.thenorthface.de/shop/de/tnf-de/damen-jacken/damen-fanorak-2-0-jacke-3sv8?variationId=L48")
        chrome.find_element_by_css_selector('span.close').click()
        time.sleep(3)

        chrome.find_element_by_css_selector('.fitanalytics__button-text').click()
        # chrome.find_element_by_css_selector('#fitanalytics__button img').click()
        time.sleep(2)



if __name__ == '__main__':
    unittest.main()