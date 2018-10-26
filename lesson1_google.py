# -*- coding: utf-8 -*-
import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def create_chrome_driver():
    home_dir = os.getenv('HOME')
    driver_location = os.path.join(home_dir, 'bin', 'chromedriver')
    return webdriver.Chrome(driver_location)


@pytest.fixture
def driver(request):
    chrome = create_chrome_driver()
    request.addfinalizer(chrome.quit)
    return chrome


def test_google(driver: webdriver.Chrome):
    driver.get("http://google.com")
    driver.find_element_by_name("q").send_keys('в чем смысл жизни', Keys.ENTER)
    WebDriverWait(driver, 10).until(EC.title_contains("в чем смысл жизни"))
