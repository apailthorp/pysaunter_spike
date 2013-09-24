__author__ = 'apailthorp'

from saunter.po.webdriver.page import Page
from selenium.webdriver.common.action_chains import ActionChains
from saunter.ConfigWrapper import ConfigWrapper as cfg_wrapper
from locators import locators

class ClipCard(Page):

    def __init__(self, driver):
        self.driver = driver
        self.config = cfg_wrapper().config

    def wait_until_idle(self):
        self.wait_for_available(locators['idle'])
        return self

    def close_clipcard(self):
        self.wait_until_idle()
        closeButton = self.driver.find_element_by_locator(locators['clipcard_close'])
        closeButton.click()

    def next_face(self):
        self.wait_until_idle()
        print self.driver.find_element_by_locator("css=.active .control").get_attribute('innerhtml')
        next_button = self.driver.find_element_by_locator(locators['clipcard_next'])
        hover = ActionChains(self.driver).move_to_element(next_button)
        hover.click(self.driver.find_element_by_locator(locators['clipcard_next_active']))

