__author__ = 'apailthorp'

locators = {
    'idle': 'css=.ng-scope.ready.idle',
    'username': "css=input[name='username']",
    'password': 'css=input[name="password"]',
    'submit': 'css=input[name="submit"]',
    'gear': 'css=.has-settings .settings-menu .label',
}

from clipcard_app_base_page import ClipCardAppBasePage as Page
from saunter.ConfigWrapper import ConfigWrapper as cfg_wrapper

class LoginPage(Page):

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.driver.set_window_size(1024,800)

    def open(self):
        self.driver.get(self.config.get('Selenium', 'base_url'))
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

