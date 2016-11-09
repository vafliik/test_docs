from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class MessagePanel(BasePage):
    """
    Page Objects that represents the (left side) Message Panel
    """

    # Locators
    _chatbox_input = By.XPATH, '//input[contains(@id,"Expressyourself")]'

    _huma_response = By.CSS_SELECTOR, 'span.huma-response'

    # Dynamic locators
    _huma_response_by_text = By.XPATH, '//span//*[contains(@class, "huma-response")][contains(text(),{})]'

    def type(self, value):
        """
        Type value into the message box input field
        and confirms it by Enter key
        :param value: value to be entered (str)
        """
        chat_input = self.wait_for_element(*self._chatbox_input)
        chat_input.send_keys(value + Keys.ENTER)

    def last_huma_response(self):
        last_response = self.driver.find_elements(*self._huma_response)[-1]
        self.highlight(last_response)
        return last_response.text

    def wait_for_number_of_replies_to_be(self, expected_number):
        self.wait_for_number_of_elements(*self._huma_response, expected_number=expected_number)