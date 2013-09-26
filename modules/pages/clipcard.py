__author__ = 'apailthorp'

from clipcard_app_base_page import ClipCardAppBasePage as Page
from selenium.webdriver.common.action_chains import ActionChains
from saunter.ConfigWrapper import ConfigWrapper as cfg_wrapper

locators = {
    'clipcard_close': 'css=.active .control.close',
    'clipcard_prev': 'css=.active .control.prev[style="display: none;"]',
    'clipcard_next': 'css=.active .control.next[style="display: none;"]',
    'clipcard_prev_active': 'css=.active .control.prev[style="display: inline-block;"]',
    'clipcard_next_active': 'css=.active .control.next[style="display: inline-block;"]',
}


class ClipCard(Page):

    def __init__(self, driver):
        super(ClipCard, self).__init__(driver)


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

