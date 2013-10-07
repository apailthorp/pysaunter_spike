__author__ = 'apailthorp'

locators = {
    'idle': '.ng-scope.ready.idle',
}

import time
from saunter.po.webdriver.page import Page
from saunter.ConfigWrapper import ConfigWrapper as cfg_wrapper
from selenium.webdriver.common.by import By
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ClipCardAppBasePage(Page):

    def __init__(self, driver):
        self.driver = driver
        self.config = cfg_wrapper().config

    def wait_until_idle(self):
        _local = 'idle'
        time.sleep(1)
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME,'idle')))
        self.sleep_if_chrome()
        return self

    def sleep_if_chrome(self):
        if self.driver.desired_capabilities['browserName'] == DesiredCapabilities.CHROME['browserName']:
            time.sleep(1)