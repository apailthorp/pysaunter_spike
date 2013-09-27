__author__ = 'apailthorp'

from saunter.testcase.webdriver import SaunterTestCase
import pytest
from pages.login import LoginPage
from pages.desktop import DesktopPage
from pages.clipcard import ClipCard

class CheckLoginExample(SaunterTestCase):
    # def setup_method(self, method):
    #     super(CheckLoginExample, self).setup_method(method)
    #     self.driver = LoginPage(self.driver).open().wait_until_idle()

    # def teardown_method(self, method):
    #     super(CheckLoginExample, self).teardown_method(method)

    @pytest.marks('demo')
    def test_try_stuff(self):

        users = [
            #{"name": "a_user",
            # "password": "test"
            #},
            #{"name": "b_user",
            # "password": "testtest"
            #},
            #{"name": "c_user",
            # "password": "testtest"
            #},
            #{"name": "d_user",
            # "password": "testtest"
            #},
            #{"name": "e_user",
            # "password": "testtest"
            #},
            {"name": "f_user",
            "password": "testtest"
            },
            {"name": "g_user",
             "password": "testtest"
            },
            #{"name": "h_user",
            # "password": "testtest"
            #},
            #{"name": "i_user",
            # "password": "testtest"
            #},
            #{"name": "j_user",
            # "password": "testtest"
            #},
            #{"name": "m_user1",
            # "password": "testtesttest"
            #},
        ]

        Login = LoginPage(self.driver).open().wait_until_idle()
        assert(Login.login("g_user", "testtest"))
        Desktop = DesktopPage(self.driver).wait_until_idle()
        assert(Desktop.logout())

        for i in range(1,100):
            for someUser in users:
                user = someUser["name"]
                password = someUser["password"]
                print 'Iteration: ' + i.__str__() + ' logging in as: ' + user
                assert(Login.login(user, password))

                clipCardTitles = Desktop.getClipCardTitles()
                print 'ClipCard titles count: %s' % len(clipCardTitles)

                print 'scroll the search results'
                Desktop.scrollPanel(9)

                clipCardTitles = Desktop.getClipCardTitles()
                print 'ClipCard titles count: %s' % len(clipCardTitles)

                print 'scroll the search results'
                Desktop.scrollPanel(9)

                clipCardTitles = Desktop.getClipCardTitles()
                print 'ClipCard titles count: %s' % len(clipCardTitles)

                print 'scroll the search results'
                Desktop.scrollPanel(9)

                clipCardTitles = Desktop.getClipCardTitles()
                print 'ClipCard titles count: %s' % len(clipCardTitles)

                #print 'Some ClipCard titles'
                #clipCardTitles = Desktop.getClipCardTitles()
                #i = 0
                #for someClipCardTitle in clipCardTitles:
                #    i += 1
                #    print "%s: %s" % (i, someClipCardTitle.text)
                #    #assert(Desktop.clickClipCardTitle(someClipCardTitle.text))

                print 'zoom out as far as we can'
                while (Desktop.zoom_enabled('out')):
                    print 'zoom out'
                    Desktop.zoom('out')

                print 'assert zoom in available'
                assert(Desktop.zoom_enabled('in'))

                print 'zoom in as far as we can'
                while (Desktop.zoom_enabled('in')):
                    print 'zoom in'
                    Desktop.zoom('in')

                print 'assert zoom out available'
                assert(Desktop.zoom_enabled('out'))

                print 'reset the search'
                assert(Desktop.resetSearch())

                print 'scroll the search results'
                Desktop.scrollPanel(9)


                print 'Some ClipCard titles after search reset'
                clipCardTitles = Desktop.getClipCardTitles()
                i = 0
                for someClipCardTitle in clipCardTitles:
                    print "%s: %s" % (i, someClipCardTitle.text)
                    Desktop.scrollPanel(i)
                    i += 1
                    assert(Desktop.clickClipCardTitle(someClipCardTitle.text))
                    clipCard = ClipCard(self.driver)
                    # clipCard.next_face()
                    # clipCard.next_face()
                    clipCard.close_clipcard()

                assert(Desktop.logout())
                print 'logged out'

