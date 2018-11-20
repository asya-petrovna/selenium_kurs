import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from drivers import drivers
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
import os
from steps import login_litecart
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    chrome = drivers.create_chrome_driver()
    request.addfinalizer(chrome.quit)
    return chrome


def test_check_link_in_new_window(driver: WebDriver):
    def open_new_window(number_of_link):
        set_before = set(driver.window_handles)
        driver.find_elements_by_css_selector("#content a")[number_of_link].click()
        WebDriverWait(driver, 5).until(EC.new_window_is_opened)
        set_after = set(driver.window_handles)
        new_window = set_after - set_before
        assert len(new_window) == 1
        driver.switch_to.window(list(new_window)[0])
        time.sleep(3)
        driver.close()
        driver.switch_to.window(main_window)

    login_litecart(driver)
    driver.find_elements_by_css_selector("#app-")[2].click()
    driver.find_element_by_css_selector('.button').click()
    driver.find_element_by_css_selector("input[value = '1']").click()
    main_window = driver.current_window_handle
    for i in (1, 2, 3, 5, 6, 7, 8):
        open_new_window(i)
    driver.find_elements_by_css_selector("#content a")[4].click()
    WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    time.sleep(2)
    alert.accept()
