__author__ = 'apailthorp'

import time
from clipcard_app_base_page import ClipCardAppBasePage as Page
from selenium.webdriver.common.action_chains import ActionChains
from saunter.ConfigWrapper import ConfigWrapper as cfg_wrapper

locators = {
    'clipcard_close': 'css=.active .control.close',
    'clipcard_flip': 'css=.active .control.flip',
    'clipcard_edit': 'css=.action.method-action',
    'clipcard_edit_text': 'Edit ClipCard',
    'clipcard_cancel': 'css=.button.cancel',
    'clipcard_save': 'css=.button.save.submit'
    'clipcard_prev': 'css=.active .control.prev[style="display: none;"]',
    'clipcard_next': 'css=.active .control.next[style="display: none;"]',
    'clipcard_prev_active': 'css=.active .control.prev[style="display: inline-block;"]',
    'clipcard_next_active': 'css=.active .control.next[style="display: inline-block;"]',
}

class ClipCard(Page):

    def __init__(self, driver):
        super(ClipCard, self).__init__(driver)

    def button_click(self,locator):
        self.wait_until_idle()
        someButton = self.driver.find_element_by_locator(locators[locator])
        someButton.click()

    def close(self):
        return self.button_click('clipcard_close')

    def flip(self):
        return self.button_click('clipcard_flip')

    def edit(self):
        self.wait_until_idle()
        editButton = self.driver.find_element_by_locator(locators['clipcard_edit'])
        if editButton.text == locators['clipcard_edit_text']:
            editButton.click()
            return True
        return False

    def cancel(self):
        return self.button_click('clipcard_cancel')

    def save(self):
        return self.button_click('clipcard_save')

    def next_face(self):
        self.wait_until_idle()
        print self.driver.find_element_by_locator("css=.active .control").get_attribute('innerhtml')
        next_button = self.driver.find_element_by_locator(locators['clipcard_next'])
        hover = ActionChains(self.driver).move_to_element(next_button)
        hover.click(self.driver.find_element_by_locator(locators['clipcard_next_active']))

