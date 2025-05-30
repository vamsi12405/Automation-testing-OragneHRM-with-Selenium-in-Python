from selenium.webdriver.common.by import By
from .base_page import BasePage

class PimPage(BasePage):
    EMPLOYEE_NAME_INPUT = (By.XPATH, "//label[text()='Employee Name']/../following-sibling::div//input")
    SEARCH_BUTTON = (By.XPATH, "//button[span[text()='Search']]")
    TABLE_ROWS = (By.XPATH, "//div[@role='table']//div[@role='row']")
    def search_employee(self, name):
        self.enter_text(self.EMPLOYEE_NAME_INPUT, name)
        self.click(self.SEARCH_BUTTON)
    def found_employee(self, name):
        rows = self.driver.find_elements(*self.TABLE_ROWS)
        return any(name in r.text for r in rows)