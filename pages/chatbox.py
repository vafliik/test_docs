from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Chatbox:

    #Locators
    _chatbox_input = By.XPATH, '//input[contains(@id,"Expressyourself")]'

    _huma_response = By.CSS_SELECTOR, 'span.huma-response'

    def __init__(self, driver):
        self.driver = driver

    def type(self, value):
        chat_input = self.driver.find_element(*self._chatbox_input)
        chat_input.send_keys(value + Keys.ENTER)

    def last_huma_response(self):
        last_response = self.driver.find_elements(*self._huma_response)[-1]
        return last_response.text
