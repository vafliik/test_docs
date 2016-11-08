import pytest

from pages.chatbox import Chatbox
from utils.framework import Framework

class BaseTestClass():

    def setup_class(self):
        print("\nInit Framework\n")
        self.framework = Framework()


    @pytest.fixture(autouse=True)
    def toggle_browser(self):
        print("\nStarting browser\n")

        self.driver = self.framework.start_browser()
        self.driver.get(self.framework.base_url)

        # Associate Page objects
        self.chatbox = Chatbox(self.driver)

        yield self.toggle_browser()
        print("\nClosing browser\n")
        self.driver = self.framework.stop_browser()

