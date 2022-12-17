import selenium
from selenium.webdriver.common.by import By

from AbstractClassDriverManager import AbstractClassDriverManager
from selenium import webdriver



####
#Class represent implementation  Chrome Driver Manager
#Include methods important to scrape
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



    def find_eleement(self, kindTypeSerche, phraseSerche):
        try :
            element=None
            if(kindTypeSerche == "CLASS"):
                element=self.getDriver().find_element(By.CLASS_NAME, phraseSerche)
            elif(kindTypeSerche == "ID"):
                element =self.getDriver().find_element(By.ID, phraseSerche)
            return element
        except selenium.common.exceptions.NoSuchElementException:
            print("We dont found element , Check your code !")
            return element

    def find_elements(self, kindTypeSerche, phraseSerche):
        try :
            elements=[]
            if(kindTypeSerche=="CLASS"):
                elements = self.getDriver().find_elements(By.CLASS_NAME, phraseSerche)
            elif(kindTypeSerche == "ID"):
                elements = self.getDriver().find_elements(By.ID, phraseSerche)
        except selenium.common.exceptions.NoSuchElementException:
            print("We dont found element , Check your code !")
            return elements










