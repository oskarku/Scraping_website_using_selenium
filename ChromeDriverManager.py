import selenium

from AbstractClassDriverManager import AbstractClassDriverManager
from selenium import webdriver



####
#Class represent implementation  Chrome Driver Manager

####
class ChromeDriverManagerLoc(AbstractClassDriverManager):


    def startService(self):
        pass

    def stopService(self):
        pass

    def createDriver(self):
        self.driver = webdriver.Chrome(executable_path='/Users/dawidlefuk/Desktop/selenium/webdriver/chrome/chromedriver')
        self.driver.implicitly_wait(15)
        self.driver.set_page_load_timeout(50)
        return self.driver













