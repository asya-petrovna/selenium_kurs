import os
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def create_gecko_driver():
    home_dir = os.getenv('HOME')
    return Firefox(executable_path=os.path.join(home_dir, 'bin', 'geckodriver'))


@pytest.fixture
def driver(request):
    firefox = create_gecko_driver()
    request.addfinalizer(firefox.quit)
    return firefox


def test_successful_login(driver: WebDriver):  # type hint for IDE
    driver.get("http://localhost:8080/litecart/admin/login.php")
    driver.find_element_by_name("username").send_keys('admin', Keys.TAB)
    driver.find_element_by_name("password").send_keys('admin', Keys.ENTER)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'sidebar')))
