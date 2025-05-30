from selenium.webdriver.common.by import By
from .base_page import BasePage

class MyInfoPage(BasePage):
    HEADER = (By.XPATH, "//h6[text()='Personal Details']")
    def is_loaded(self):
        return self.is_displayed(self.HEADER)