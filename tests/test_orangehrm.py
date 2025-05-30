import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
print("NEW PYTHONPATH:", sys.path)
import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage
from pages.leave_page import LeavePage
from pages.pim_page import PimPage
from pages.myinfo_page import MyInfoPage
from pages.time_page import TimePage
from pages.directory_page import DirectoryPage

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver
    driver.quit()

def test_valid_login(driver):
    driver.delete_all_cookies()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login = LoginPage(driver)
    driver.implicitly_wait(10)  # Add this line for implicit wait
    login.login("Admin", "admin123")
    assert "dashboard" in driver.current_url or "dashboard" in driver.page_source

def test_invalid_login(driver):
    try:
        driver.delete_all_cookies()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        login = LoginPage(driver)
        login.login("wrong", "wrongpass")
        assert "Invalid credentials" in login.get_error_message()
    except:
        print(login.get_error_message())
        assert "Invalid credentials" in login.get_error_message()

def test_logout(driver):
    driver.delete_all_cookies()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login = LoginPage(driver)
    login.login("Admin", "admin123")
    dashboard = DashboardPage(driver)
    dashboard.logout()
    assert "auth/login" in driver.current_url

def test_admin_search_user(driver):
    driver.delete_all_cookies()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login = LoginPage(driver)
    login.login("Admin", "admin123")
    dashboard = DashboardPage(driver)
    dashboard.goto_admin()

    # --- Place the code here ---
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    wait = WebDriverWait(driver, 10)
    username_box = wait.until(
        EC.visibility_of_element_located((By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]"))
    )
    username_box.clear()
    username_box.send_keys("lolita")

    search_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")))
    search_button.click()

    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div[@class='oxd-table-body']"), "lolita"))
    assert "lolita" in driver.page_source

def test_admin_add_user(driver):
    driver.delete_all_cookies()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login = LoginPage(driver)
    login.login("Admin", "admin123")
    dashboard = DashboardPage(driver)
    dashboard.goto_admin()
    admin = AdminPage(driver)
    username = "user1234"
    admin.add_user(
        "ESS",             # user_role
        "Paul Collings",   # employee_name (must be a valid employee in the system)
        username,          # username
        "Enabled",         # status
        "Password@123"     # password
    )
    assert admin.is_user_created()