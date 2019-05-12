import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from drivers import drivers
from selenium.webdriver.common.by import By


# drivers.create_chrome_driver()


# from drivers import DriverFactory
# DriverFactory().create_chrome_driver()

@pytest.fixture
def driver(request):
    chrome=drivers.create_chrome_driver()
    request.addfinalizer(chrome.quit)
    return chrome


def test_check_list(driver: WebDriver):
    driver.get("http://localhost:8080/litecart/admin/login.php")
    driver.find_element_by_name("username").send_keys('admin', Keys.TAB)
    driver.find_element_by_name("password").send_keys('admin', Keys.ENTER)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'sidebar')))

    #    driver.find_element_by_css_selector("button[type='submit']").click()

    for i in range(len(get_sidebar_list(driver))):
        row=get_sidebar_list(driver)[i]
        click_and_check(driver, row.find_element_by_css_selector("a"))
        for k in range(1, len(get_sidebar_list_second_level(driver))):
            subrow=get_sidebar_list_second_level(driver)[k]
            click_and_check(driver, subrow.find_element_by_css_selector("a"))
        time.sleep(1)


def get_sidebar_list(driver):
    return driver.find_elements_by_css_selector("#app-")


def get_sidebar_list_second_level(driver):
    return driver.find_elements_by_css_selector(".docs li")


def click_and_check(driver, element):
    url_before_click=driver.current_url
    element.click()
    WebDriverWait(driver, 10).until(EC.url_changes(url_before_click))
    assert is_element_present(driver, 'h1')


def is_element_present(driver: WebDriver, selector):
    try:
        driver.find_element_by_css_selector(selector)
    except NoSuchElementException:
        return False
    return True
#    assert EC.presence_of_element_located((By.TAG_NAME, 'h1'))(driver)
#    assert len(driver.find_elements_by_tag_name('h1')) == 1
