from selenium.webdriver.common.by import By
from .base_page import BasePage

class TimePage(BasePage):
    HEADER = (By.XPATH, "//h6[text()='Time']")
    def is_loaded(self):
        return self.is_displayed(self.HEADER)