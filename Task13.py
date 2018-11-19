import pytest
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from drivers import drivers
from steps import login_as_customer


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

        if is_element_present('select'):
            select = Select(driver.find_element_by_css_selector('select'))
            select.select_by_visible_text('Small')

        driver.find_element_by_css_selector('button[name = "add_cart_product"]').click()
        close_alert_if__present()
        driver.refresh()
        #        WebDriverWait(driver, 5).until(EC.staleness_of(element))
        assert pre_quantity != driver.find_element_by_css_selector("#cart-wrapper .quantity").get_attribute(
            "textContent")
        driver.back()

    def del_item_from_cart():
        old_row = driver.find_elements_by_css_selector('#box-checkout-summary tr')[1]
        driver.find_element_by_css_selector('button[name = "remove_cart_item"]').click()
        WebDriverWait(driver, 3).until(EC.staleness_of(old_row))

    def is_element_present(selector):
        try:
            driver.find_element_by_css_selector(selector)
            return True
        except NoSuchElementException:
            return False

    def close_alert_if__present():
        try:
            WebDriverWait(driver, 5).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            pass

    login_as_customer(driver)
    for i in range(3):
        add_item_to_cart()
    driver.find_element_by_xpath(f"//*[contains(text(), 'Checkout')]").click()
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#order_confirmation-wrapper')))
    while is_element_present('#box-checkout-summary'):
        del_item_from_cart()

    driver.get('http://localhost:8080/litecart/en/')
    assert driver.find_element_by_css_selector("#cart-wrapper .quantity").get_attribute(
            "textContent") == '0'
