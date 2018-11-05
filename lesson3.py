import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from drivers import drivers
from selenium.webdriver.common.by import By

#drivers.create_chrome_driver()


# from drivers import DriverFactory
# DriverFactory().create_chrome_driver()

@pytest.fixture
def driver(request):
    chrome = drivers.create_chrome_driver()
    request.addfinalizer(chrome.quit)
    return chrome


def test_check_list(driver: WebDriver):
    driver.get("http://localhost:8080/litecart/admin/login.php")
    driver.find_element_by_name("username").send_keys('admin', Keys.TAB)
    driver.find_element_by_name("password").send_keys('admin', Keys.ENTER)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'sidebar')))

    #    driver.find_element_by_css_selector("button[type='submit']").click()

    for i in range(len(get_sidebar_list(driver))):
        row = get_sidebar_list(driver)[i]
        row.find_element_by_css_selector("a").click()
        WebDriverWait(driver, 10).until(EC.url_changes("http://localhost:8080/litecart/admin/"))
        time.sleep(1)


def get_sidebar_list(driver):
    return driver.find_elements_by_css_selector("#app-")

