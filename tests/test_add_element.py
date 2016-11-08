import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from tests.base_test import BaseTestClass


class TestAddElement(BaseTestClass):

    def test_add_button(self):
        ''' Verify that Button element can be added by typing into the chatbox input'''
        self.message_panel.type('Add FlatButton')

        self.message_panel.wait_for_number_of_replies_to_be(1)

        assert self.message_panel.last_huma_response() == 'OK, I added a FlatButton'