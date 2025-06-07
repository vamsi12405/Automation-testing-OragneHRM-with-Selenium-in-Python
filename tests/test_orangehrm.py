from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from OrangeHRM.pages.login_page import LoginPage
from OrangeHRM.pages.dashboard_page import DashboardPage
from OrangeHRM.pages.user_page import AddUserPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_valid_login(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    login = LoginPage(driver)
    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "oxd-userdropdown-name"))
    )
    print(driver.current_url)
    dashboard = DashboardPage(driver)
    assert dashboard.is_dashboard_visible()

def test_invalid_login(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    login = LoginPage(driver)
    login.enter_username("fake")
    login.enter_password("fake")
    login.click_login()
    assert "Invalid credentials" in login.get_error_message()

def test_logout(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    login = LoginPage(driver)
    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login()

    dashboard = DashboardPage(driver)
    dashboard.logout()
    assert "login" in driver.current_url.lower()
