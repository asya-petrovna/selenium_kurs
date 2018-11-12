from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def login_litecart(driver: WebDriver):
    driver.get("http://localhost:8080/litecart/admin/login.php")
    driver.find_element_by_name("username").send_keys('admin', Keys.TAB)
    driver.find_element_by_name("password").send_keys('admin', Keys.ENTER)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'sidebar')))
