from saunter.po.webdriver.page import Page as SaunterPage

from saunter.po import timeout_seconds
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time

class Page(SaunterPage):
    def __init__(self, driver):
        super(type(self), self).__init__(driver)
        
