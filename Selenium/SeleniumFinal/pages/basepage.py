from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import LogGen

loggger = LogGen.loggen()

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # ===== Generic element actions =====
    def get_element(self, locator, condition=EC.visibility_of_element_located):
        loggger.info(f'Locating an element: {locator}')
        return self.wait.until(condition(locator))

    def click(self, locator):
        loggger.info(f'Clicking an element: {locator}')
        self.get_element(locator, EC.element_to_be_clickable).click()

    def type(self, locator, text):
        loggger.info(f'Typing in the element: {locator}')
        element = self.get_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        loggger.info(f'Getting the element: {locator}')
        return self.get_element(locator).text

    def is_visible(self, locator):
        loggger.info(f'Checking is visible: {locator}')
        return self.get_element(locator).is_displayed()