from saunter.po.webdriver.page import Page as SaunterPage

class Page(SaunterPage):
    def __init__(self, driver):
        super(type(self), self).__init__(driver)
        
