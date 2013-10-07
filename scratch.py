__author__ = 'apailthorp'

# Some notes for interacting with selenium using ipython

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import DesiredCapabilities
caps = DesiredCapabilities.CHROME
driver = WebDriver(command_executor='http://127.0.0.1:4444/wd/hub', desired_capabilities=caps)
driver.set_window_size(1024,800)
driver.get('https://qa.app.mtoc.us')
titles = driver.find_elements_by_css_selector('.clipcards .title')
titles[2].click()
for someTitle in titles: print someTitle.__repr__
print len(titles)
