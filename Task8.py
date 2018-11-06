import pytest
import time
from selenium.common.exceptions import NoSuchElementException

from drivers import drivers
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture
def driver(request):
    chrome=drivers.create_chrome_driver()
    request.addfinalizer(chrome.quit)
    return chrome


def test_check_goods(driver: WebDriver):
    driver.get("http://localhost:8080/litecart")
    for i in range(len(get_goods_list(driver))):
        row = get_goods_list(driver)[i]
        assert is_element_present(driver, ".sticker")
        time.sleep(1)
        assert len(row.find_elements_by_css_selector('.sticker')) == 1


def get_goods_list(driver):
    return driver.find_elements_by_css_selector('li.product.column.shadow.hover-light')


def is_element_present(driver, selector):
    try:
        driver.find_elements_by_css_selector(selector)
    except NoSuchElementException:
        return False
    return True
# def is_element_present(driver: WebDriver, row.find_element_by_css_selector('.sticker')):
# assert is_element_present(driver, row.find_element_by_css_selector('.sticker'))
