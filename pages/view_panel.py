from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class ViewPanel(BasePage):

    # Locators
    _card = By.CSS_SELECTOR, 'div.card-example'

    _card_content = By.CSS_SELECTOR, _card[1] + ' > div > div:nth-child(2) > div'

    def expand_card(self):
        self.wait_for_element(*self._card).click()

    def card_content(self):
        return self.wait_for_element(*self._card_content)

    def card_content_elements(self):
        return self.card_content().find_elements(By.XPATH, '*')
