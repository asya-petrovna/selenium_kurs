import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from drivers import drivers
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
import os
from steps import login_litecart


@pytest.fixture
def driver(request):
    chrome = drivers.create_chrome_driver()
    request.addfinalizer(chrome.quit)
    return chrome


def test_create_new_product(driver: WebDriver):
    def find_input(selector):
        return driver.find_element_by_css_selector(f'input[{selector}]')

    def find_inputs(selector):
        return driver.find_elements_by_css_selector(f'input[{selector}]')

    def get_select_by_name(name):
        return Select(driver.find_element_by_css_selector(f"select[name = '{name}']"))

    login_litecart(driver)
    driver.find_elements_by_css_selector("#app-")[1].click()
    driver.find_elements_by_css_selector("a.button")[1].click()
    time.sleep(2)

    find_inputs("type = 'radio'")[1].click()
    item_name = f'{int(time.time())}cowboy_duck'
    find_input("name = 'name[en]'").send_keys(item_name)
    find_input("name = 'code'").send_keys('777')
    find_inputs("type = 'checkbox'")[0].click()
    find_inputs("type = 'checkbox'")[1].click()
    find_input("value = '1-1'").click()
    find_input("name = 'quantity'").send_keys('100')
    get_select_by_name('sold_out_status_id').select_by_index(0)

    path_to_file = os.path.join(os.getcwd(), 'cowboy_duck.jpg')
    find_input("type = 'file'").send_keys(path_to_file)
    find_input("name = 'date_valid_from'").send_keys('16122018')
    find_input("name = 'date_valid_to'").send_keys('16122022')
    time.sleep(3)
    driver.find_elements_by_css_selector(".index a")[1].click()
    time.sleep(3)
    get_select_by_name('manufacturer_id').select_by_visible_text('ACME Corp.')
    find_input("name = 'keywords'").send_keys('rubber duck')
    find_input("name = 'short_description[en]'").send_keys('cowboy style duck')
    driver.find_element_by_css_selector(".trumbowyg-editor").send_keys('really cool cowboy style duck')
    find_input("name = 'head_title[en]'").send_keys('COWBOY DUCK')
    find_input("name = 'meta_description[en]'").send_keys('COWBOY DUCK')
    driver.find_elements_by_css_selector(".index a")[3].click()
    time.sleep(3)
    find_input("name = 'purchase_price'").send_keys('5')
    get_select_by_name('purchase_price_currency_code').select_by_visible_text('US Dollars')
    find_input("name = 'gross_prices[USD]'").clear()
    find_input("name = 'gross_prices[USD]'").send_keys('5')
    find_input("name = 'gross_prices[EUR]'").clear()
    find_input("name = 'gross_prices[EUR]'").send_keys('4')
    time.sleep(3)
    driver.find_element_by_css_selector("button[name = 'save']").click()
    time.sleep(5)

    driver.find_element_by_css_selector('#doc-catalog').click()
    driver.find_elements_by_css_selector('.dataTable a')[1].click()
    assert driver.find_element_by_xpath(f"//*[contains(text(), '{item_name}')]")
