from selenium.webdriver.common.by import By

class AdminPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_admin(self):
        self.driver.find_element(By.LINK_TEXT, "Admin").click()

    def search_user(self, name):
        self.driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']").send_keys(name)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def get_result_rows(self):
        return self.driver.find_elements(By.XPATH, "//div[@role='row']")