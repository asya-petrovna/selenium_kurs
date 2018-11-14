import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from drivers import drivers
import re
import time


@pytest.fixture
def driver(request):
    chrome = drivers.create_chrome_driver()
    request.addfinalizer(chrome.quit)
    return chrome


def test_main_page_normal_price(driver: WebDriver):
    driver.get("http://localhost:8080/litecart")
    price_color = driver.find_element_by_css_selector('#box-campaigns .regular-price').value_of_css_property("color")
    red, green, blue, alpha = parse_color(price_color)
    assert is_grey(red, green, blue)
    assert driver.find_element_by_css_selector('#box-campaigns s.regular-price'), 'regular price is not crossed'


def test_main_page_sale_price(driver: WebDriver):
    driver.get("http://localhost:8080/litecart")
    price_color = driver.find_element_by_css_selector('#box-campaigns .campaign-price').value_of_css_property("color")
    red, green, blue, alpha = parse_color(price_color)
    assert is_red(red, green, blue)
    assert driver.find_element_by_css_selector('#box-campaigns strong.campaign-price')

def test_good_page_normal_price(driver: WebDriver):
    driver.get("http://localhost:8080/litecart")
    driver.find_element_by_css_selector('#box-campaigns a').click()
    price_color = driver.find_element_by_css_selector('.regular-price').value_of_css_property("color")
    red, green, blue, alpha = parse_color(price_color)
    assert is_grey(red, green, blue)


def test_good_page_sale_price(driver: WebDriver):
        driver.get("http://localhost:8080/litecart")
        driver.find_element_by_css_selector('#box-campaigns a').click()
        price_color = driver.find_element_by_css_selector('.campaign-price').value_of_css_property(
            "color")
        red, green, blue, alpha = parse_color(price_color)
        assert is_red(red, green, blue)


def price_color_string(price_color):

    red, green, blue, alpha = parse_color(price_color)
    return red, green, blue, alpha


def parse_color(color_string):
    """Parse string of format rgba(NNN, NNN, NNN, N) into a tuple of integers (R, G, B, A)"""
    return tuple(re.findall(r'\d+', color_string))


def is_grey(red, green, blue):
    return red == green and green == blue


def is_red(red, green, blue):
    return red != '0' and green == '0' and blue == '0'


