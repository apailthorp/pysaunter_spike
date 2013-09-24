
__author__ = 'apailthorp'

from saunter.po.webdriver.page import Page
from saunter.ConfigWrapper import ConfigWrapper as cfg_wrapper
from locators import locators

class LoginPage(Page):

    def __init__(self, driver):
        self.driver = driver
        self.driver.set_window_size(1024,800)
        self.config = cfg_wrapper().config

    def open(self):
        self.driver.get(self.config.get('Selenium', 'base_url'))
        return self

    def wait_until_idle(self):
        self.wait_for_available(locators['idle'])
        return self

    def login(self, name, pwd):
        self.wait_until_idle()
        driver = self.driver
        driver.find_element_by_locator(locators['username']).send_keys(name)
        driver.find_element_by_locator(locators['password']).send_keys(pwd)
        driver.find_element_by_locator(locators['submit']).click()
        self.wait_until_idle()
        if not(self.driver.is_element_present(locators['gear'])):
            return False
        return True

