__author__ = 'apailthorp'

from saunter.testcase.webdriver import SaunterTestCase
from random import choice
import pytest
from modules.pages.login import LoginPage
from modules.pages.desktop import DesktopPage
from modules.pages.clipcard import ClipCard

class CheckExamples(SaunterTestCase):
    # def setup_method(self, method):
    #     super(CheckLoginExample, self).setup_method(method)
    #     self.driver = LoginPage(self.driver).open().wait_until_idle()

    # def teardown_method(self, method):
    #     super(CheckLoginExample, self).teardown_method(method)

    users = [
        {"name": "a_user",
        "password": "testtesttest"
        },
        {"name": "b_user",
        "password": "testtest"
        },
        #{"name": "c_user",
        #"password": "testtest"
        #},
        #{"name": "d_user",
        #"password": "testtest"
        #},
        #{"name": "e_user",
        #"password": "testtest"
        #},
        #{"name": "f_user",
        #"password": "testtest"
        #},
        #{"name": "g_user",
        #"password": "testtest"
        #},
        #{"name": "h_user",
        #"password": "testtest"
        #},
        #{"name": "i_user",
        #"password": "testtest"
        #},
        #{"name": "j_user",
        #"password": "testtest"
        #},
        #{"name": "m_user1",
        #"password": "testtesttest"
        #},
        #{"name": "manycards",
        #"password": "manycards"
        #},
    ]

    @pytest.marks('thumbs')
    def test_login_thumbnails(self):

        Login = LoginPage(self.driver).open().wait_until_idle()
        Desktop = DesktopPage(self.driver).wait_until_idle()

        for j in range(1):
            # randomly select a user
            someUser = choice(CheckExamples.users)
            username = someUser["name"]
            password = someUser["password"]
            print 'Iteration: ' + j.__str__() + ' logging in as: ' + username
            assert(Login.login(username, password))

            Titles = Desktop.getClipCardTitlesNoScroll()
            lenthTitles = len(Titles)
            print 'ClipCard titles count: %s' % lenthTitles

            maxLengthTitles = 0
            panelCount = 0
            while (lenthTitles > maxLengthTitles):
                maxLengthTitles = lenthTitles
                print 'scroll the search results'
                # scroll down three additional panes to force a page fetch
                panelCount += 3
                Desktop.scrollPanel(panelCount)
                Titles = Desktop.getClipCardTitlesNoScroll()
                lenthTitles = len(Titles)
                print 'ClipCard titles count: %s' % len(Titles)

            print 'Some ClipCard thumbnails'
            clipCardThumbnails = Desktop.getClipCardThumbnails(username, password)
            print 'Thumbnail count: ' + len(clipCardThumbnails).__str__()
            i = 0
            thumbnail404Count = 0
            thumbnail200Count = 0
            for someClipCardThumbnail in clipCardThumbnails:
                i += 1
                thumbnailUrl = someClipCardThumbnail.imageUrl
                thumbnailUrlStatus = someClipCardThumbnail.imageUrlStatus
                print "%s: %s: status:%s " % (i,thumbnailUrl,thumbnailUrlStatus)
                if thumbnailUrlStatus == 404: thumbnail404Count += 1
                if thumbnailUrlStatus == 200: thumbnail200Count += 1

            assert(Desktop.logout())
            print 'Thumbnail 200 count: ' + thumbnail200Count.__str__()
            print 'Thumbnail 404 count: ' + thumbnail404Count.__str__()
            assert thumbnail404Count==0, "expecting 0 404s from thumbnails, found %s" % thumbnail404Count
            print 'logged out'

    @pytest.marks('demo', 'clickAll')
    def test_zoom(self):


        Login = LoginPage(self.driver).open().wait_until_idle()
        # assert(Login.login("g_user", "testtest"))
        Desktop = DesktopPage(self.driver).wait_until_idle()
        # assert(Desktop.logout())

        for j in range(1):
            # randomly select a user
            someUser = choice(CheckExamples.users)
            username = someUser["name"]
            password = someUser["password"]
            print 'Iteration: ' + j.__str__() + ' logging in as: ' + username
            assert(Login.login(username, password))

            clipCardTitles = Desktop.getClipCardTitlesNoScroll()
            print 'ClipCard titles count without scroll: %s' % len(clipCardTitles)

            #maxLengthTitles = 0
            #panelCount = 0
            #while (lenthTitles > maxLengthTitles):
            #    maxLengthTitles = lenthTitles
            #    print 'scroll the search results'
            #    # scroll down three additional panes to force a page fetch
            #    panelCount += 3
            #    Desktop.scrollPanel(panelCount)
            #    Titles = Desktop.getClipCardTitlesNoScroll()
            #    lenthTitles = len(Titles)

            print 'Getting all ClipCard titles'
            clipCardTitles = Desktop.getClipCardTitlesAll()
            print 'ClipCard titles count: %s' % len(clipCardTitles)
            print 'Some ClipCard titles'
            i = 0
            for someClipCardTitle in clipCardTitles:
                i += 1
                print "%s: %s, " % (i, someClipCardTitle.text),
                if i % 5 == 0: print
                #assert(Desktop.clickClipCardTitle(someClipCardTitle.text))
            print

            for direction in ['out','in']:
                print 'assert zoom ' + direction + ' available'
                assert(Desktop.zoom_enabled(direction))

                print 'zoom '+ direction + ' as far as we can, but without paging search list'
                while (Desktop.zoom_enabled(direction)):
                    Desktop.zoom(direction)
                    print 'Zoomed ' + direction + ', length of list of ClipCards: %s' % len(Desktop.getClipCardTitlesAll()).__str__()

            print 'reset the search'
            assert(Desktop.resetSearch())

            print 'assert zoom in available'
            assert(Desktop.zoom_enabled('in'))

            print 'assert zoom out available'
            assert(Desktop.zoom_enabled('out'))

            print 'Some ClipCard titles after search reset'
            Titles = Desktop.getClipCardTitlesAll()
            i = 1
            for someClipCardTitle in Titles:
                print "%s: %s, " % (i, someClipCardTitle.text),
                if i % 5 == 0: print
                assert(Desktop.clickClipCardTitle(someClipCardTitle.text))
                clipCard = ClipCard(self.driver)
                # clipCard.next_face()
                # clipCard.next_face()
                clipCard.close()
                i += 1

            print

            assert(Desktop.logout())
            print 'logged out'

    @pytest.marks('deleteAll')
    def test_delete(self):

        Login = LoginPage(self.driver).open().wait_until_idle()
        Desktop = DesktopPage(self.driver).wait_until_idle()

        for someUser in CheckExamples.users:

            username = someUser["name"]
            password = someUser["password"]
            print 'Logging in as: ' + username

            assert(Login.login(username, password))

            Titles = Desktop.getClipCardTitlesAll()
            lengthTitles = len(Titles)
            print 'ClipCard titles count: %s' % lengthTitles

            for someClipCardTitle in Titles:
                assert(Desktop.clickClipCardTitle(someClipCardTitle.text))
                clipCard = ClipCard(self.driver)
                assert clipCard.flip()
                assert clipCard.edit()
                assert clipCard.flip()
                assert clipCard.close()

            assert(Desktop.logout())

