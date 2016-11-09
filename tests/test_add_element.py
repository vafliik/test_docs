from tests.base_test import BaseTest


class TestAddElement(BaseTest):

    def test_add_button(self):
        """
        Verify that Button element can be added by typing into the chatbox input
        """

        self.message_panel.type('Add FlatButton')

        self.message_panel.wait_for_number_of_replies_to_be(1)

        assert self.message_panel.last_huma_response() == 'OK, I added a FlatButton'

        self.view_panel.expand_card()

        buttons = self.view_panel.card_content_buttons()

        assert len(buttons) == 1

        assert buttons[0].text == 'BUTTON'

    def test_add_button_with_label(self):
        """
        Verify that Button element with custom label
        can be added by typing into the chatbox input
        """

        self.message_panel.type('Add FlatButton called Sheldon')

        self.message_panel.wait_for_number_of_replies_to_be(1)

        assert self.message_panel.last_huma_response() == 'OK, I added a FlatButton called Sheldon'

        self.view_panel.expand_card()

        buttons = self.view_panel.card_content_buttons()

        assert len(buttons) == 1

        assert buttons[0].text == 'SHELDON'
