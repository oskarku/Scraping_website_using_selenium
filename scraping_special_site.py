import time

import now as now
import selenium
import speedtest
import timeunit
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time
import datetime


##
# This script scraping price  about website
####
#


# print (str(st.download()))
import DriverType
from DriverManagerFactory import DriverManagerFactory


# driver = webdriver.Chrome(executable_path='/Users/dawidlefuk/Desktop/selenium/webdriver/chrome/chromedriver')
# print ("below is type driver")
#
# driver.implicitly_wait(15)
# driver.set_page_load_timeout(50)
# url = 'https://mera.eu'
# driver.get(url)
# searcher = driver.find_element(By.CLASS_NAME, 'menu_search__input')
# searcher.send_keys("miska wc")
# button_search = driver.find_element(By.CLASS_NAME,'menu_search__submit')
# button_search.click()
#
#
#
#
# time.sleep(2.4)
# all_products_reserche = driver.find_elements(By.CLASS_NAME, "product")
# print(f"Number of products: {len(all_products_reserche)}")
# dateTimeTest = datetime.datetime.now()
#
# all_product_an_price = []
# try:
#     for product in all_products_reserche:
#         price_elm = product.find_element(By.CLASS_NAME, 'price')
#         name_elm = product.find_element(By.CLASS_NAME, 'product__name')
#         price = price_elm.text
#         name = name_elm.text
#         print("-------")
#         print(name)
#         # print(price)
#         print("-----")
#         all_product_an_price.append({'name': name, 'price': price,'url_website':url ,'dateTime':dateTimeTest})
#     print(all_product_an_price)
#     with open('/Users/dawidlefuk/Desktop/udemy/Selenium web drive/SeleniumPyCrashCourse/employee_file2.csv', mode='w') as csv_file:
#         fieldnames = ['name', 'price' , 'url_website','dateTime']
#         writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#         writer.writeheader()
#         for product in all_product_an_price:
#             writer.writerow(product)
#
#         writer.writerows(all_product_an_price)
#
# except selenium.common.exceptions.TimeoutException:
#     print("Masz slaby internet ")


##---------------------
#Improve code style implement  Factory Pattern Test (litle fake implementation):
#https://www.vinsguru.com/selenium-webdriver-design-patterns-in-test-automation-factory-pattern/
####


#implement chrom selenium driver \


class FactoryPatternTestScrape:


    def __init__(self):
        self.driver=None
        self.driverManager = None

    def beforeMethod(self):
        if(self.driverManager==None):
            driveManagerFactory = DriverManagerFactory()
            managerLocaly = driveManagerFactory.getManager("CHROME")

            self.driverManager= managerLocaly
            print(type(self.driverManager))
            self.driver=self.driverManager.getDriver()
            print(type(self.driver))


    def afterMethode(self):
        self.driverManager.quiteDriver

    def testMerawebsite(self):
        self.driver.implicitly_wait(15)
        self.driver.set_page_load_timeout(50)
        url = 'https://mera.eu'
        self.driver.get(url)
        searcher = self.driver.find_element(By.CLASS_NAME, 'menu_search__input')
        searcher.send_keys("miska wc")
        button_search = self.driver.find_element(By.CLASS_NAME, 'menu_search__submit')
        button_search.click()

test1=FactoryPatternTestScrape()
test1.beforeMethod()
test1.testMerawebsite()


print(DriverType.WebDriverEnum.CHROME.name)





        






