from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    def is_dashboard_visible(self):
        return "dashboard" in self.driver.current_url.lower()

    def logout(self):
        self.driver.find_element(By.CLASS_NAME, "oxd-userdropdown-name").click()
        self.driver.find_element(By.XPATH, "//a[text()='Logout']").click()