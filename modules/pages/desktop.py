__author__ = 'apailthorp'

import time
from saunter.po.webdriver.page import Page
from saunter.ConfigWrapper import ConfigWrapper as cfg_wrapper
from locators import locators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0


class DesktopPage(Page):

    def __init__(self, driver):
        self.driver = driver
        self.config = cfg_wrapper().config

    def open(self):
        self.driver.get(self.config.get('Selenium', 'base_url'))
        return self

    def wait_until_idle(self):
        self.wait_for_available(locators['idle'])
        return self

    def open_close_gear(self):
        self.wait_until_idle()
        gear = self.driver.find_element_by_locator(locators['gear'])
        gear.click()
        time.sleep(2)
        self.wait_until_idle()
        gear.click()
        return True

    def zoom_enabled(self, inOrOut):
        print 'Testing for zoom ' + inOrOut + ' enabled'
        self.wait_until_idle()
        print 'done waiting'
        try:
            print 'trying for zoom ' + inOrOut
            self.driver.find_element_by_locator(locators['zoom_' + inOrOut])
        except NoSuchElementException:
            print 'zoom ' + inOrOut + ' not found'
            return False
        try:
            print 'Checking if zoom ' + inOrOut + ' disabled'
            self.driver.find_element_by_locator(locators['zoom_' + inOrOut + '_disabled'])
            return False
        except NoSuchElementException:
            print 'zoom ' + inOrOut + ' disabled'
            pass
        return True

    # Attempts zoom out, returns true if able, false if zoom out disabled
    def zoom(self, inOrOut):
        self.wait_until_idle()
        try:
            zoom_control = self.driver.find_element_by_locator(locators['zoom_' + inOrOut])
        except NoSuchElementException:
            return False
        else:
            zoom_control.click()
            return True

