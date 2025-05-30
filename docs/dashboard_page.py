from selenium.webdriver.common.by import By
from .base_page import BasePage

class DashboardPage(BasePage):
    LOGOUT_DROPDOWN = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
    LOGOUT_BUTTON = (By.LINK_TEXT, "Logout")
    ADMIN_TAB = (By.XPATH, "//span[text()='Admin']")
    LEAVE_TAB = (By.XPATH, "//span[text()='Leave']")
    PIM_TAB = (By.XPATH, "//span[text()='PIM']")
    MYINFO_TAB = (By.XPATH, "//span[text()='My Info']")
    TIME_TAB = (By.XPATH, "//span[text()='Time']")
    DIRECTORY_TAB = (By.XPATH, "//span[text()='Directory']")

    def logout(self):
        self.click(self.LOGOUT_DROPDOWN)
        self.click(self.LOGOUT_BUTTON)

    def goto_admin(self):
        self.click(self.ADMIN_TAB)

    def goto_leave(self):
        self.click(self.LEAVE_TAB)

    def goto_pim(self):
        self.click(self.PIM_TAB)

    def goto_myinfo(self):
        self.click(self.MYINFO_TAB)

    def goto_time(self):
        self.click(self.TIME_TAB)

    def goto_directory(self):
        self.click(self.DIRECTORY_TAB)