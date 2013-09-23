from saunter.po.webdriver.page import Page as SaunterPage

from saunter.po import timeout_seconds
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time
from locators import locators

class Page(SaunterPage):
    def __init__(self, driver):
        super(type(self), self).__init__(driver)
        
    def wait_until_idle(self):
        self.wait_for_available(locators['idle'])
        return self
