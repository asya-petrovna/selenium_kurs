import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from drivers import drivers
import re


@pytest.fixture
def driver(request):
    chrome = drivers.create_chrome_driver()
    request.addfinalizer(chrome.quit)
    return chrome


def test_main_page_normal_price(driver: WebDriver):
    driver.get("http://localhost:8080/litecart")
    check_color(driver, '#box-campaigns .regular-price', is_grey)
    is_price_crossed(driver, '#box-campaigns .regular-price')
#    assert driver.find_element_by_css_selector('#box-campaigns s.regular-price'), 'regular price is not crossed'


def test_good_page_normal_price(driver: WebDriver):
    driver.get("http://localhost:8080/litecart")
    driver.find_element_by_css_selector('#box-campaigns a').click()
    check_color(driver, '.regular-price', is_grey)
    is_price_crossed(driver, '.regular-price')


def test_main_page_sale_price(driver: WebDriver):
    driver.get("http://localhost:8080/litecart")
    check_color(driver, '#box-campaigns .campaign-price', is_red)
    assert driver.find_element_by_css_selector('#box-campaigns strong.campaign-price')
#    is_price_bold(driver, '#box-campaigns .campaign-price')


def test_good_page_sale_price(driver: WebDriver):
    driver.get("http://localhost:8080/litecart")
    driver.find_element_by_css_selector('#box-campaigns a').click()
    check_color(driver, '.campaign-price', is_red)
    assert driver.find_element_by_css_selector('strong.campaign-price')
#   is_price_bold(driver, '.campaign-price')

def is_price_crossed(driver, selector):
    assert 'line-through' in driver.find_element_by_css_selector(selector).value_of_css_property('text-decoration')


#def is_price_bold(driver, selector):
#    assert 'bold' in driver.find_element_by_css_selector(selector).value_of_css_property('font-weight')


def check_color(driver, price_selector, is_expected_color):
    price_color = driver.find_element_by_css_selector(price_selector).value_of_css_property("color")
    red, green, blue, alpha = parse_color(price_color)
    assert is_expected_color(red, green, blue)


def parse_color(color_string):
    """Parse string of format rgba(NNN, NNN, NNN, N) into a tuple of integers (R, G, B, A)"""
    return tuple(re.findall(r'\d+', color_string))


def is_grey(red, green, blue):
    return red == green and green == blue


def is_red(red, green, blue):
    return red != '0' and green == '0' and blue == '0'
