import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from drivers import drivers


@pytest.fixture(params=[
    drivers.create_chrome_driver,
    drivers.create_gecko_driver
])
def driver(request):
    driver = request.param()
    request.addfinalizer(driver.quit)
    driver.get("http://localhost:8080/litecart")
    return driver


def test_check_goods(driver: WebDriver):
    """Task 10 a, names"""
    name_main = driver.find_element_by_css_selector('#box-campaigns .name').get_attribute('textContent')
    price_main = driver.find_element_by_css_selector('#box-campaigns .regular-price').get_attribute('textContent')
    sale_main = driver.find_element_by_css_selector('#box-campaigns .campaign-price').get_attribute('textContent')

    driver.find_element_by_css_selector('#box-campaigns a').click()
    name_good = driver.find_element_by_css_selector('h1.title').get_attribute('textContent')
    price_good = driver.find_element_by_css_selector('.information .regular-price').get_attribute('textContent')
    sale_good = driver.find_element_by_css_selector('.information .campaign-price').get_attribute('textContent')

    assert name_main == name_good, 'Names are different!'
    assert price_main == price_good, 'Prices are different!'
    assert sale_main == sale_good, 'Sale prices are different!'


def test_size_prises(driver: WebDriver):
    """Task 10 d, size of price"""
    main_page_regular_price_size = driver.find_element_by_css_selector('#box-campaigns .regular-price').size
    main_page_sale_price_size = driver.find_element_by_css_selector('#box-campaigns .campaign-price').size
    driver.find_element_by_css_selector('#box-campaigns a').click()
    good_page_regular_price_size = driver.find_element_by_css_selector('.regular-price').size
    good_page_sale_price_size = driver.find_element_by_css_selector('.campaign-price').size

    assert main_page_regular_price_size['height'] < main_page_sale_price_size['height']
    assert good_page_regular_price_size['height'] < good_page_sale_price_size['height']
