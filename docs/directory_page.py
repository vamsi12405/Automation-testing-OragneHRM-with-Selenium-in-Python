from selenium.webdriver.common.by import By
from .base_page import BasePage

class DirectoryPage(BasePage):
    EMPLOYEE_NAME_INPUT = (By.XPATH, "//input[contains(@placeholder,'Type for hints')]")
    JOB_TITLE_DROPDOWN = (By.XPATH, "//label[text()='Job Title']/../following-sibling::div//div[contains(@class,'oxd-select-text')]")
    LOCATION_DROPDOWN = (By.XPATH, "//label[text()='Location']/../following-sibling::div//div[contains(@class,'oxd-select-text')]")
    SEARCH_BUTTON = (By.XPATH, "//button[span[text()='Search']]")
    TABLE_ROWS = (By.XPATH, "//div[@role='table']//div[@role='row']")

    def search_employee(self, name):
        self.enter_text(self.EMPLOYEE_NAME_INPUT, name)
        self.click(self.SEARCH_BUTTON)

    def search_job_title(self, job_title):
        self.click(self.JOB_TITLE_DROPDOWN)
        self.click((By.XPATH, f"//div[contains(@role,'option')]//span[text()='{job_title}']"))
        self.click(self.SEARCH_BUTTON)

    def search_location(self, location):
        self.click(self.LOCATION_DROPDOWN)
        self.click((By.XPATH, f"//div[contains(@role,'option')]//span[text()='{location}']"))
        self.click(self.SEARCH_BUTTON)

    def has_results(self):
        rows = self.driver.find_elements(*self.TABLE_ROWS)
        return len(rows) > 1  # header row + results