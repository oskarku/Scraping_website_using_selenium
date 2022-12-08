from AbstractClassDriverManager import AbstractClassDriverManager
from selenium import webdriver

class ChromeDriverManagerLoc(AbstractClassDriverManager):


    def startService(self):
        pass

    def stopService(self):
        pass

    def createDriver(self):
        return webdriver.Chrome(executable_path='/Users/dawidlefuk/Desktop/selenium/webdriver/chrome/chromedriver')





