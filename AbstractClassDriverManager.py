from abc import abstractmethod, ABC

import selenium
from selenium import webdriver

class AbstractClassDriverManager(ABC):
    def __init__(self):
        self.driver=None


    @abstractmethod
    def startService(self):
        pass

    @abstractmethod
    def stopService(self):
        pass

    @abstractmethod
    def createDriver(self):
        pass


    def quiteDriver(self):
        if(self.driver!=None):
            self.driver.quite()
            self.driver=None


    def getDriver(self):
        if(self.driver==None):
            self.driver=self.createDriver()
        return self.driver








