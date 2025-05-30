from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).clear()
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def is_displayed(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()

    def wait_for_url(self, url):
        self.wait.until(EC.url_contains(url))

    def click(self, locator):
        try:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
        except Exception as e:
            self.driver.save_screenshot('click_failed.png')
            raise

    def enter_text(self, locator, text):
        try:
            el = self.wait.until(EC.visibility_of_element_located(locator))
            el.clear()
            el.send_keys(text)
        except Exception as e:
            self.driver.save_screenshot('enter_text_failed.png')
            raise