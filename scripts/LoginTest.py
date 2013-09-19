__author__ = 'apailthorp'

from saunter.testcase.webdriver import SaunterTestCase
import pytest
from pages.login import LoginPage
from pages.desktop import DesktopPage

class CheckLoginExample(SaunterTestCase):
    def setup_method(self, method):
        super(CheckLoginExample, self).setup_method(method)
        self.uiLogin = LoginPage(self.driver).open().wait_until_idle()

    # def teardown_method(self, method):
    #     super(CheckLoginExample, self).teardown_method(method)

    @pytest.marks('demo')
    def test_login_gear_zoom(self):

        print 'Logging in'
        assert(self.uiLogin.login('g_user', 'testtest'))

        self.desktop = DesktopPage(self.driver).wait_until_idle()

        assert(self.desktop.open_close_gear())

        print ('zoom out as far as we can')
        while (self.desktop.zoom_enabled('out')):
            print ('zoom out')
            self.desktop.zoom('out')

        print ('test zoom in available')
        assert(self.desktop.zoom_enabled('in'))

        print ('zoom in as far as we can')
        while (self.desktop.zoom_enabled('in')):
            print ('zoom in')
            self.desktop.zoom('in')

        print ('test zoom out available')
        assert(self.desktop.zoom_enabled('out'))

