import time

import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from drivers import drivers
from steps import login_litecart


@pytest.fixture
def driver(request):
    chrome = drivers.create_chrome_driver()
    request.addfinalizer(chrome.quit)
    return chrome


def test_log_reader(driver: WebDriver):
    def is_element_present(selector, root):
        try:
            root.find_element_by_css_selector(selector)
            return True
        except NoSuchElementException:
            return False

    def is_folder(table_row):
        return is_element_present(".fa-folder", table_row) or is_element_present(".fa-folder-open", table_row)

    def get_list_of_goods():
        list_of_content = driver.find_element_by_css_selector(".dataTable")
        return list_of_content.find_elements_by_css_selector('tr:not(.header):not(.footer)')

    login_litecart(driver)
    driver.find_elements_by_css_selector("#app-")[1].click()
    driver.find_element_by_xpath(f"//*[contains(text(), 'Rubber Ducks')]").click()
    driver.find_element_by_xpath(f"//*[contains(text(), 'Subcategory')]").click()

    for i in range(len(get_list_of_goods())):
        list_of_goods = get_list_of_goods()
        row = list_of_goods[i]
        if is_folder(row):
            continue
        row.find_elements_by_css_selector("a")[0].click()
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.NAME, 'name[en]')))
        #        name.find_element_by_css_selector('a').click()
        assert not driver.get_log('browser'), f'unexpected log messages on iteration {i}'
        driver.back()
