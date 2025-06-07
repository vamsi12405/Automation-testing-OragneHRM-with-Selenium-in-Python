from selenium.webdriver.common.by import By

class AddUserPage:
    def __init__(self, driver):
        self.driver = driver

    def click_add_user(self):
        self.driver.find_element(By.XPATH, "//button[contains(.,'Add')]").click()

    def fill_form(self, employee_name, username, password):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']").send_keys(employee_name)
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.NAME, "confirmPassword").send_keys(password)

    def save(self):
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()