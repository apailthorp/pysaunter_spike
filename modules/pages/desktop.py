__author__ = 'apailthorp'

locators = {
    'idle': 'css=.idle',
    'logout': ".ui.popout.menu.active a.link[href='/account/logout/']",
    'username': "css=input[name='username']",
    'gear': 'css=.has-settings .settings-menu .label',
    'zoom_out': 'css=a.leaflet-control-zoom-out',
    'zoom_out_disabled': 'css=.leaflet-control-zoom-out.leaflet-control-zoom-disabled',
    'zoom_in': 'css=a.leaflet-control-zoom-in',
    'zoom_in_disabled': 'css=a.leaflet-control-zoom-in.leaflet-control-zoom-disabled',
    'clipcard_titles': 'css=.clipcards .title',
    'reset_search_disabled': 'css=button.reset[style="display: none;"]',
    'reset_search': 'css=button.reset',
}

import time
from clipcard_app_base_page import ClipCardAppBasePage as Page
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DesktopPage(Page):

    def __init__(self, driver):
        super(DesktopPage, self).__init__(driver)

    def logout(self):
        self.wait_until_idle()
        gear = self.driver.find_element_by_locator(locators['gear'])
        gear.click()
        # logout = self.driver.find_element_by_locator(locators['logout'])
        logout = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR,locators['logout'])))
        logout.click()
        time.sleep(2)
        self.wait_until_idle()
        if not(self.driver.is_element_present(locators['username'])):
            return False
        return True

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
        print 'testing zoom ' + inOrOut
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
        time.sleep(1)
        self.wait_until_idle()
        print 'clicking zoom '  + inOrOut
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
                # Sleep necessary due to bug with chrome driver:
                # http://code.google.com/p/selenium/issues/detail?id=2766
                # & http://code.google.com/p/chromedriver/issues/detail?id=22
                # & http://code.google.com/p/chromedriver/issues/detail?id=28
                # time.sleep(1)
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

    # def getPanelHeight(self):
    #     return self.driver.execute_script("return $('.panel.sidebar').height()")

    def scrollPanel(self, scrollHeight):
        script = "var listPage = function(page) { var panel = $('.panel.sidebar'), top = (page - 1) * panel.height(); panel.scrollTop(top); }; listPage(%s);" % scrollHeight
        self.driver.execute_script(script)
        self.wait_until_idle()
