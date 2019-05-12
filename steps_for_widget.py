import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class UsedSteps(unittest.TestCase):

    def setUp(self):
        home_dir = os.getenv('HOME')
        chromedriver_location = os.path.join(home_dir, 'bin', 'chromedriver')
        self.chrome = webdriver.Chrome(chromedriver_location)

    def TearDown(self):

    def find_and_click_on_element(self, selector):
        chrome = self.chrome
        chrome.find_element_by_css_selector(selector).click()

    def wait_until_element_presense(self, method, selector):
        chrome = self.chrome
        WebDriverWait(chrome, 10).until(EC.presence_of_element_located((method, selector)))
