from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from cart_page import CartPage
from drivers import drivers
from goods_page import GoodsPage
from main_page import MainShopPage


def login_litecart(driver: WebDriver):
    driver.get("http://localhost:8080/litecart/admin/login.php")
    driver.find_element_by_name("username").send_keys('admin', Keys.TAB)
    driver.find_element_by_name("password").send_keys('admin', Keys.ENTER)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'sidebar')))


def login_as_customer_old(driver: WebDriver):
    driver.get('http://localhost:8080/litecart/en/')
    driver.find_element_by_css_selector("input[name = 'email']").clear()
    driver.find_element_by_css_selector("input[name = 'email']").send_keys("asya.gush@gmail.com", Keys.TAB)
    driver.find_element_by_css_selector("input[name = 'password']").clear()
    driver.find_element_by_css_selector("input[name = 'password']").send_keys("123456", Keys.TAB)
    driver.find_element_by_css_selector("button[name = 'login']").click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'list-vertical')))


class App:
    def __init__(self, driver=drivers.create_chrome_driver()):
        self.main_page = MainShopPage(driver)
        self.cart_page = CartPage(driver)
        self.goods_page = GoodsPage(driver)

    def login_as_customer(self):
        self.main_page.login('asya.gush@gmail.com', '123456')

    def quit(self):
        self.main_page.driver.quit()
