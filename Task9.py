import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from steps import login_litecart
from drivers import drivers


@pytest.fixture
def driver(request):
    chrome = drivers.create_chrome_driver()
    request.addfinalizer(chrome.quit)
    return chrome


def test_is_country_sorted(driver: WebDriver):
    login_litecart(driver)
    driver.get("http://localhost:8080/litecart/admin/?app=countries&doc=countries")
    rows = get_list(driver)
    countries = [row.find_element_by_css_selector("a").get_attribute('textContent') for row in rows]
    assert is_sorted(countries)
    #   assert all(countries[i] <= countries[i + 1] for i in range(len(countries) - 1))

    for i in range(len(get_list(driver))):
        row = get_list(driver)[i]
        zone_text = row.find_elements_by_css_selector("td")[5].get_attribute('textContent')
        if int(zone_text) > 0:
            row.find_element_by_css_selector("a").click()
            table = driver.find_element_by_css_selector("#table-zones")
            table_rows = table.find_elements_by_css_selector('tr:not(.header)')
            get_zone_name = lambda r: r.find_elements_by_css_selector('td')[2].get_attribute('textContent')
            zone_names = [get_zone_name(table_row) for table_row in table_rows]
            print(zone_names)
            # assert all(zone_names[i] <= zone_names[i + 1] for i in range(len(zone_names) - 1))
            assert is_sorted(zone_names[:-1])
            driver.get("http://localhost:8080/litecart/admin/?app=countries&doc=countries")


def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))


def get_list(driver):
    return driver.find_elements_by_css_selector(".row")
