import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from steps import login_litecart
from drivers import drivers


@pytest.fixture
def driver(request):
    chrome = drivers.create_chrome_driver()
    request.addfinalizer(chrome.quit)
    return chrome


def test_is_zones_sorted(driver: WebDriver):
    login_litecart(driver)
    driver.get("http://localhost:8080/litecart/admin/?app=geo_zones&doc=geo_zones")
    for i in range(len(find_rows(driver))):
        driver.find_element_by_css_selector("a").click()
        selects = driver.find_elements_by_css_selector("select")
        assert is_sorted(get_all_selected_options(selects))
        driver.back()


def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))


def get_all_selected_options(selects):
    return [get_selected_option(select) for select in selects]


def get_selected_option(select):
    for option in select.find_elements_by_css_selector('option'):
        if option.get_attribute('selected'):
            return option.get_attribute('label')


def find_rows(root):
    return root.find_elements_by_css_selector(".row")
