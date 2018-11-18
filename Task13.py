import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from drivers import drivers
from steps import login_as_customer
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


@pytest.fixture
def driver(request):
    chrome = drivers.create_chrome_driver()
    request.addfinalizer(chrome.quit)
    return chrome


def test_add_and_dell_item_to_cart(driver: WebDriver):
    def add_item_to_cart():
        element = driver.find_element_by_css_selector("#cart-wrapper .quantity")
        pre_quantity = element.get_attribute("textContent")
        driver.find_elements_by_css_selector("#box-most-popular a")[0].click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, 'add_cart_product')))
        time.sleep(1)
        if is_select_present('select'):
            select = Select(driver.find_element_by_css_selector('select'))
            select.select_by_visible_text('Small')

        driver.find_element_by_css_selector('button[name = "add_cart_product"]').click()
        alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert.accept()
        driver.refresh()
        WebDriverWait(driver, 5).until(EC.staleness_of(element))
        assert pre_quantity != driver.find_element_by_css_selector("#cart-wrapper .quantity").get_attribute(
            "textContent")
        driver.back()

    def is_select_present(selector):
        try:
            driver.find_element_by_css_selector(selector)
        except NoSuchElementException:
            return False
        return True

    login_as_customer(driver)
    for i in range(3):
        add_item_to_cart()
    driver.find_element_by_css_selector()
    driver.find_element_by_xpath(f"//*[contains(text(), 'Checkout')]").click()
