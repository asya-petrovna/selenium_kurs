import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from drivers import drivers
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    chrome = drivers.create_chrome_driver()
    request.addfinalizer(chrome.quit)
    return chrome

def test_registration(driver: WebDriver):
    driver.get('http://localhost:8080/litecart/en/')
    driver.find_element_by_css_selector(".content [name = 'login_form'] a").click()
    driver.find_element_by_css_selector("input[name = 'firstname']").send_keys("Asya", Keys.TAB)
    driver.find_element_by_css_selector("input[name = 'lastname']").send_keys("Isaeva", Keys.TAB)
    driver.find_element_by_css_selector("input[name = 'address1']").send_keys("Rochowstrasse", Keys.SPACE, "14", Keys.ENTER)
    driver.find_element_by_css_selector("input[name = 'postcode']").send_keys("10245", Keys.TAB)
    driver.find_element_by_css_selector("input[name = 'city']").send_keys("Berlin", Keys.TAB)
    select = Select(driver.find_element_by_css_selector("select[name = 'country_code']"))
    select.select_by_visible_text('United States')
    email = generate_email()
    driver.find_element_by_css_selector("input[name = 'email']").send_keys(email, Keys.TAB)
    driver.find_element_by_css_selector("input[name = 'phone']").send_keys("123456789", Keys.TAB)
#    driver.find_element_by_css_selector("input[type = 'checkbox']").clear()
    if driver.find_element_by_css_selector("input[type = 'checkbox']").get_attribute('value') == 1:
        driver.find_element_by_css_selector("input[type = 'checkbox']").click()
    driver.find_element_by_css_selector("input[name = 'password']").send_keys("123456", Keys.TAB)
    driver.find_element_by_css_selector("input[name = 'confirmed_password']").send_keys("123456", Keys.TAB)
    driver.find_element_by_css_selector("button[name = 'create_account']").click()
    time.sleep(2)
#    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'notice errors')))
    select_zone = Select(driver.find_element_by_css_selector("select[name = 'zone_code']"))
    select_zone.select_by_visible_text('Minnesota')
    driver.find_element_by_css_selector("input[name = 'password']").send_keys("123456", Keys.TAB)
    driver.find_element_by_css_selector("input[name = 'confirmed_password']").send_keys("123456", Keys.TAB)
    driver.find_element_by_css_selector("button[name = 'create_account']").click()
    time.sleep(2)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'list-vertical')))
    driver.find_elements_by_css_selector("#box-account .content .list-vertical a")[3].click()
    time.sleep(2)
    driver.find_element_by_css_selector("input[name = 'email']").clear()
    driver.find_element_by_css_selector("input[name = 'email']").send_keys(email, Keys.TAB)
    driver.find_element_by_css_selector("input[name = 'password']").clear()
    driver.find_element_by_css_selector("input[name = 'password']").send_keys("123456", Keys.TAB)
    driver.find_element_by_css_selector("button[name = 'login']").click()
    time.sleep(2)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'list-vertical')))
    driver.find_elements_by_css_selector("#box-account .content .list-vertical a")[3].click()
    time.sleep(10)


def generate_email():
    return f'g{int(time.time())}@gmail.com'
