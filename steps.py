from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def login_litecart(driver: WebDriver):
    driver.get("http://localhost:8080/litecart/admin/login.php")
    driver.find_element_by_name("username").send_keys('admin', Keys.TAB)
    driver.find_element_by_name("password").send_keys('admin', Keys.ENTER)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'sidebar')))


def login_as_customer(driver: WebDriver):
    driver.get('http://localhost:8080/litecart/en/')
    driver.find_element_by_css_selector("input[name = 'email']").clear()
    driver.find_element_by_css_selector("input[name = 'email']").send_keys("asya.gush@gmail.com", Keys.TAB)
    driver.find_element_by_css_selector("input[name = 'password']").clear()
    driver.find_element_by_css_selector("input[name = 'password']").send_keys("123456", Keys.TAB)
    driver.find_element_by_css_selector("button[name = 'login']").click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'list-vertical')))


def is_element_present(driver: WebDriver, selector):
    try:
        driver.find_element_by_css_selector(selector)
        return True
    except NoSuchElementException:
        return False


def close_alert_if__present(driver: WebDriver):
    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
    except TimeoutException:
        pass
