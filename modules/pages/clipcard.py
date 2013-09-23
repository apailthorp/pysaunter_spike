__author__ = 'apailthorp'

import time
from saunter.po.webdriver.page import Page
from saunter.ConfigWrapper import ConfigWrapper as cfg_wrapper
from locators import locators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

class ClipCard(Page):

    def wait_until_idle(self):
        self.wait_for_available(locators['idle'])
        return self

    def __init__(self, driver):
        self.driver = driver
        self.config = cfg_wrapper().config

    def close_clipcard(self):
        self.wait_until_idle()
        closeButton = self.driver.find_element_by_locator(locators['close_clipcard'])
        closeButton.click()

