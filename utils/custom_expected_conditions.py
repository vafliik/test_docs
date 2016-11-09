"""
Custom "Expected Conditions" which are generally useful
within webdriver tests.
"""
from selenium.common.exceptions import WebDriverException


class number_of_elements_to_be():
    """
    An expectation for the number of located
    elements to be a certain value.
    """

    def __init__(self, locator, num_elements):
        self.locator = locator
        self.num_elements = num_elements

    def __call__(self, driver):
        elements = _find_elements(driver, self.locator)
        return len(elements) == self.num_elements

def _find_elements(driver, by):
    try:
        return driver.find_elements(*by)
    except WebDriverException as e:
        raise e