import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from tests.base_test import BaseTestClass


class TestAddElement(BaseTestClass):

    def test_add_button(self):
        ''' Verify that Button element can be added by typing into the chatbox input'''
        self.chatbox.type('Add FlatButton')
        assert self.chatbox.last_huma_response() == 'OK, I added a FlatButton'