__author__ = 'apailthorp'

from saunter.testcase.webdriver import SaunterTestCase
import pytest
from pages.login import LoginPage
from pages.desktop import DesktopPage

class CheckLoginExample(SaunterTestCase):
    # def setup_method(self, method):
    #     super(CheckLoginExample, self).setup_method(method)
    #     self.u = LoginPage(self.driver).open().wait_until_loaded()
    #
    # def teardown_method(self, method):
    #     super(CheckLoginExample, self).teardown_method(method)


    @pytest.marks('demo')
    def test_login_show_gear(self):
        u = LoginPage(self.driver).open().wait_until_loaded()
        assert(u.login("g_user", "testtest"))

        d = DesktopPage(self.driver).wait_until_loaded()
        assert(d.open_close_gear())

