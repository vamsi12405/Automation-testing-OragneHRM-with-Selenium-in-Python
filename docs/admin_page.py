from selenium.webdriver.common.by import By
from .base_page import BasePage

class AdminPage(BasePage):
    USERNAME_SEARCH = (By.XPATH, "//label[text()='Username']/../following-sibling::div/input")
    SEARCH_BUTTON = (By.XPATH, "//button[span[text()='Search']]")
    ADD_BUTTON = (By.XPATH, "//button[normalize-space()='Add']")
    TABLE_ROWS = (By.XPATH, "//div[@role='table']//div[@role='row']")
    USERNAME_CELL = (By.XPATH, "//div[@role='table']//div[@role='row']//div[2]")
    # Add User fields
    USER_ROLE_DROPDOWN = (By.XPATH, "//label[text()='User Role']/../following-sibling::div//div[contains(@class,'oxd-select-text')]")
    EMPLOYEE_NAME_INPUT = (By.XPATH, "//input[@placeholder='Type for hints...']")
    ADD_USERNAME_INPUT = (By.XPATH, "//label[text()='Username']/../following-sibling::div/input")
    STATUS_DROPDOWN = (By.XPATH, "//label[text()='Status']/../following-sibling::div//div[contains(@class,'oxd-select-text')]")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Password']/../following-sibling::div/input")
    CONFIRM_PASSWORD_INPUT = (By.XPATH, "//label[text()='Confirm Password']/../following-sibling::div/input")
    SAVE_BUTTON = (By.XPATH, "//button[normalize-space()='Save']")
    SUCCESS_TOAST = (By.XPATH, "//div[contains(@class,'oxd-toast')]")

    def search_user(self, username):
        self.enter_text(self.USERNAME_SEARCH, username)
        self.click(self.SEARCH_BUTTON)

    def user_exists(self, username):
        # After search, check if username exists in results
        rows = self.driver.find_elements(*self.USERNAME_CELL)
        return any(username == r.text for r in rows)

    def add_user(self, user_role, employee_name, username, status, password):
        self.click(self.ADD_BUTTON)
        self.click(self.USER_ROLE_DROPDOWN)
        self.click((By.XPATH, f"//div[contains(@role,'option')]//span[text()='{user_role}']"))
        self.enter_text(self.EMPLOYEE_NAME_INPUT, employee_name)
        self.enter_text(self.ADD_USERNAME_INPUT, username)
        self.click(self.STATUS_DROPDOWN)
        self.click((By.XPATH, f"//div[contains(@role,'option')]//span[text()='{status}']"))
        self.enter_text(self.PASSWORD_INPUT, password)
        self.enter_text(self.CONFIRM_PASSWORD_INPUT, password)
        self.click(self.SAVE_BUTTON)

    def is_user_created(self):
        return self.is_displayed(self.SUCCESS_TOAST)