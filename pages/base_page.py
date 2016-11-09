from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils import custom_expected_conditions
from utils.framework import Framework

import time


class BasePage:
    """
    Class with shared methods / locators for extending Page Objects
    """

    def __init__(self, driver):
        self.driver = driver
        self.framework = Framework()
        self.timeout = int(self.framework.get_opt('timeout'))

    def wait_for_element(self, *locator, timeout=None):
        """
        Wait until the element is located

        :param locator: element locator (tuple)
        :param timeout: seconds to wait before failing (int)
        :return:
        """
        timeout = timeout or self.timeout
        element = WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(locator)
        )
        self.highlight(element)
        return element

    def wait_for_number_of_elements(self, *locator, expected_number, timeout=None):
        """
        Wait until required number of specified elements is located in the page

        :param locator: element locator (tuple)
        :param expected_number: number of elements (int)
        :param timeout: seconds to wait before failing (int)
        :return: true if all elements found
        :raises: TimeoutException if elements not found within the time limit
        """
        timeout = timeout or self.timeout
        return WebDriverWait(self.driver, timeout).until(
            custom_expected_conditions.number_of_elements_to_be(locator, expected_number)
        )

    def get_child_elements(self, parent_element):
        return parent_element.find_elements(By.XPATH, '*')

    def highlight(self, element):
        """Highlights (blinks) a Selenium Webdriver element"""

        def apply_style(s):
            self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                       element, s)

        original_style = element.get_attribute('style')
        apply_style("background: yellow; border: 2px solid red;")
        time.sleep(.3)
        apply_style(original_style)
