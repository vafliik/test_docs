from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils import custom_expected_conditions
from utils.framework import Framework


class BasePage:
    """
    Class with shared methods / locators for extending Page Objects
    """

    def __init__(self, driver):
        self.driver = driver
        self.framework = Framework()
        self.timeout = int(self.framework.get_opt('timeout'))

    def wait_for_element(self, *locator, timeout=None):
        timeout = timeout or self.timeout
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    def wait_for_number_of_elements(self, locator, expected_number, timeout=None):
        timeout = timeout or self.timeout
        return WebDriverWait(self.driver, timeout).until(
            custom_expected_conditions.number_of_elements_to_be(locator, expected_number)
        )