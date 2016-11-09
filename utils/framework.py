import configparser
import os

import time

import pytest
from selenium import webdriver


class Framework:

    def __init__(self):
        self.project_root = os.path.join(os.path.dirname(__file__), os.pardir)

        self.test_timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        self.epoch = int(time.time())

        # get configs
        self.configs = self.load_configs()

        self.base_url = self.get_opt('base_url')

    def start_browser(self, browser_type=None):
        """
        Start browser. Currently supported are Chrome and Firefox
        Require latest selenium webdrivers to be installed and added in system path.
        If no browser type specified, the value from .properties is used

        :param browser_type: 'Chrome' for Chrome browser, any other value for Firefox (default)
        :return: Selenium Webdriver
        """

        if not browser_type:
            browser_type = self.get_opt('browser_type')

        if browser_type.lower() == 'chrome':
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Firefox()

        return self.driver

    def stop_browser(self):
        """
        Quits the browser used for testing
        """
        self.driver.quit()

    def load_configs(self):
        """
        Load variables from .properties configuration files. If local_execution is true in local_config file, function
        return both local config dict and server confgi dict. Otherwise function returns only server config dict.

        :return: list with config dictionaries
        :raises ValueError: if config path does not exist
        """

        config_path = os.path.join(self.project_root, 'config')
        if not os.path.exists(config_path):
            raise ValueError('Configuration path does not exist (%s)' % config_path)

        # load local config variables
        config = configparser.ConfigParser()
        local_config = os.path.join(config_path, 'local_config.properties')
        config.read(local_config)
        configs = (config.defaults())

        return configs

    def get_opt(self, key):
        """
        Read the value from configuration (.properties) file

        :param key: configuration key
        :return: configuration value
        """

        return self.configs[key]
