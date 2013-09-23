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

    # Checks and reports state of zoom in or out control
    def zoom_enabled(self, inOrOut):
        self.wait_until_idle()
        try:
            self.driver.find_element_by_locator(locators['zoom_' + inOrOut])
        except NoSuchElementException:
            return False
        try:
            self.driver.find_element_by_locator(locators['zoom_' + inOrOut + '_disabled'])
            return False
        except NoSuchElementException:
            pass
        return True

    # Attempts operate zoom in or out, returns true if able, false if zoom out disabled
    def zoom(self, inOrOut):
        self.wait_until_idle()
        try:
            zoom_control = self.driver.find_element_by_locator(locators['zoom_' + inOrOut])
        except NoSuchElementException:
            return False
        else:
            zoom_control.click()
            return True

    def getClipCardTitles(self):
        self.wait_until_idle()
        return self.driver.find_elements_by_locator(locators['clipcard_titles'])

    # TODO: Find a better way to get the target ClipCard to click on
    def clickClipCardTitle(self, someClipCardTitle):
        self.wait_until_idle()
        someClipCardTitles = self.getClipCardTitles()
        for testTitle in someClipCardTitles:
            if testTitle.text == someClipCardTitle:
                someClipCard = testTitle
                someClipCard.click()
                return True
        return False

    def resetSearch(self):
        self.wait_until_idle()
        try:
            disabled_reset = self.driver.find_element_by_locator(locators['reset_search_disabled'])
            return False
        except NoSuchElementException:
            try:
                enabled_reset = self.driver.find_element_by_locator(locators['reset_search'])
                enabled_reset.click()
            except NoSuchElementException:
                return False
            finally:
                return True
        return False
