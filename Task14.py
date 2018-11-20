import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from drivers import drivers
from steps import login_litecart
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    chrome = drivers.create_chrome_driver()
    request.addfinalizer(chrome.quit)
    return chrome


def test_check_link_in_new_window(driver: WebDriver):
    def open_new_window(external_link):
        main_window = driver.current_window_handle
        set_before = set(driver.window_handles)
        external_link.click()
        WebDriverWait(driver, 5).until(EC.new_window_is_opened)
        set_after = set(driver.window_handles)
        new_window = set_after - set_before
        assert len(new_window) == 1
        driver.switch_to.window(list(new_window)[0])
        driver.close()
        driver.switch_to.window(main_window)

    login_litecart(driver)
    driver.find_elements_by_css_selector("#app-")[2].click()
    driver.find_element_by_css_selector('.button').click()
    links = driver.find_elements_by_css_selector(".fa-external-link")
    for link in links:
        open_new_window(link)
