from selenium import webdriver
from fixture.searchhelper import Searchhelper

class Application:
    def __init__(self, browser, baseurl):
        if browser == 'chrome':
            self.wd = webdriver.Chrome(executable_path=r'C:\Users\admin\AppData\Local\Google\Chrome\Application\chromedriver.exe')
        elif browser == 'firefox':
            self.wd = webdriver.Firefox(executable_path=r'C:\Users\admin\AppData\Local\Google\Chrome\Application\chromedriver.exe')
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(5)
        self.wd.maximize_window()
        self.baseurl = baseurl
        self.search = Searchhelper(self)

    def open_olx_page(self):
        wd = self.wd
        wd.get(self.baseurl)

    def destroy(self):
        self.wd.quit()


