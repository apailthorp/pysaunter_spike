__author__ = 'apailthorp'

import time
from saunter.po.webdriver.page import Page
from saunter.ConfigWrapper import ConfigWrapper as cfg_wrapper
from locators import locators

class DesktopPage(Page):

    def __init__(self, driver):
        self.driver = driver
        self.config = cfg_wrapper().config

    def open(self):
        self.driver.get(self.config.get('Selenium', 'base_url'))
        return self

    def wait_until_loaded(self):
        self.wait_for_available(locators['idle'])
        return self

    def open_close_gear(self):
        self.wait_until_loaded()
        gear = self.driver.find_element_by_locator(locators['gear'])
        gear.click()
        time.sleep(2)
        self.wait_until_loaded()
        gear.click()
        return True
