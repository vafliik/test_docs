import pytest

from pages.message_panel import MessagePanel
from pages.view_panel import ViewPanel
from utils.framework import Framework

class BaseTest():

    def setup_class(self):
        print("\nInit Framework\n")
        self.framework = Framework()


    @pytest.fixture(autouse=True)
    def toggle_browser(self):
        print("\nStarting browser\n")

        self.driver = self.framework.start_browser()
        self.driver.get(self.framework.base_url)

        # Associate Page objects
        self.message_panel = MessagePanel(self.driver)
        self.view_panel = ViewPanel(self.driver)

        yield self.toggle_browser()
        print("\nClosing browser\n")
        self.driver = self.framework.stop_browser()

