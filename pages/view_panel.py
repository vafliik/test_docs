from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class ViewPanel(BasePage):
    """
    Page Objects that represents the (right side) View Panel
    """

    # Locators
    _card = By.CSS_SELECTOR, 'div.card-example'

    _card_content = By.CSS_SELECTOR, _card[1] + ' > div > div:nth-child(2) > div'

    # Card elements
    _button = By.TAG_NAME, 'button'

    def expand_card(self):
        self.wait_for_element(*self._card).click()

    def card_content(self):
        return self.wait_for_element(*self._card_content)

    def card_content_elements(self):
        return self.get_child_elements(self.card_content())

    def card_content_buttons(self):
        buttons = self.card_content().find_elements(*self._button)
        for button in buttons:
            self.highlight(button)
        return buttons

    def card_content_structure(self):
        structure = []

        for element in self.card_content_elements():
            self.highlight(element)
            if element.tag_name == 'button':
                structure.append(('Button', element.text))

            elif element.tag_name == 'hr':
                structure.append(('Divider', None))

            elif element.tag_name == 'div':

                # can be Toggle, Radio, Checkbox - they are all wrapped in div
                childs = self.get_child_elements(element)
                if childs[0].tag_name == 'input' and childs[0].get_attribute('type') == 'checkbox':
                    # TODO: can be simple Checkbox or Toggle
                    structure.append(('Checkbox', childs[1].text))

                if childs[0].tag_name == 'div':
                    # yet another wrapper, we need to go deeper
                    grand_childs = self.get_child_elements(childs[0])
                    if grand_childs[0].tag_name == 'input' and grand_childs[0].get_attribute('type') == 'radio':
                        structure.append(('RadioButton', grand_childs[1].text))

        return structure


