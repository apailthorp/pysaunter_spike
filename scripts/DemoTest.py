__author__ = 'apailthorp'

from saunter.testcase.webdriver import SaunterTestCase
import pytest
from pages.login import LoginPage
from pages.desktop import DesktopPage

class CheckLoginExample(SaunterTestCase):
    # def setup_method(self, method):
    #     super(CheckLoginExample, self).setup_method(method)
    #     self.driver = LoginPage(self.driver).open().wait_until_idle()

    # def teardown_method(self, method):
    #     super(CheckLoginExample, self).teardown_method(method)

    @pytest.marks('demo')
    def test_try_stuff(self):
        print 'logging in'
        Login = LoginPage(self.driver).open().wait_until_idle()
        assert(Login.login('g_user', 'testtest'))

        self.desktop = DesktopPage(self.driver).wait_until_idle()

        assert(self.desktop.open_close_gear())

        print 'zoom out as far as we can'
        while (self.desktop.zoom_enabled('out')):
            self.desktop.zoom('out')

        print 'assert zoom in available'
        assert(self.desktop.zoom_enabled('in'))

        print 'zoom in as far as we can'
        while (self.desktop.zoom_enabled('in')):
            self.desktop.zoom('in')

        print 'assert zoom out available'
        assert(self.desktop.zoom_enabled('out'))

        print 'reset the search'
        assert(self.desktop.resetSearch())

        print 'Some ClipCard titles'
        clipCardTitles = self.desktop.getClipCardTitles()
        for someClipCardTitle in clipCardTitles:
            print someClipCardTitle.text
            assert(self.desktop.clickClipCardTitle(someClipCardTitle.text))

