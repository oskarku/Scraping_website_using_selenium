import threading
import time
from selenium.webdriver.support import expected_conditions as EC

import now as now
import selenium
import speedtest
import timeunit
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException, InvalidSessionIdException, \
    StaleElementReferenceException, NoSuchWindowException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv
import time
import datetime
import re

##
# This script scraping price  about website
####
#


# print (str(st.download()))
from selenium.webdriver.support.wait import WebDriverWait

import DriverType
from DriverManagerFactory import DriverManagerFactory

chromedriverPath = '/Users/dawidlefuk/Desktop/selenium/webdriver/chrome/chromedriver'

class FactoryPatternTestScrape:

    def __init__(self):
        self.driver = None
        self.driverManager = None

    def beforeMethod(self):
        if (self.driverManager == None):
            driveManagerFactory = DriverManagerFactory()
            self.driverManager = driveManagerFactory.getManager("CHROME")
            self.driver = self.driverManager.getDriver()
            self.driver = webdriver.Chrome()

    def afterMethode(self):
        self.driverManager.quiteDriver

    def testMeraSearche(self, textPhrases="miska wc"):
        url = 'https://mera.eu'
        self.driver.get(url)
        searcher = self.driver.find_element(By.CLASS_NAME, 'menu_search__input')
        searcher.send_keys(textPhrases)
        button_search = self.driver.find_element(By.CLASS_NAME, 'menu_search__submit')
        button_search.click()

    # Podaje dane kluczowe np cena, rok, data  dodania(do 7 dni wstecz), przebieg od - do , marka, model i codziennie  dostaje raport na temat nowych ofert dodanych

    # css-11lsdm2
    # sum_number_page = self.driver.find_elements(By.CSS_SELECTOR, "li[data-testid='pagination-list-item']")
    # print("znalazlem ilosc stron ponizej")
    # print(sum_number_page[len(sum_number_page) - 1].text)


    def getNumberSiteOlxOferrPage(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "li[data-testid='pagination-list-item']")))
            paginationListItem=self.driver.find_elements(By.CSS_SELECTOR, "li[data-testid='pagination-list-item']")
            integerSumPage = int(paginationListItem[len(paginationListItem) - 1].text)
            return integerSumPage
        except NoSuchElementException :
            print("NoSuchElementException check your driver ")


    def restScrapOlxPreparerLink(self,dicSetupLink):
        pass
        # TODO("make method")


    def findDetalELementScrappScript(self,driverElement, dictCarsElementList):
        time.sleep(2.5)
        dataDateAndPlaceElement = driverElement.find_element(By.CSS_SELECTOR, "p[class='css-veheph er34gjf0']")
        # Oczekuj na pojawienie się elementu priceElement
        priceElement = driverElement.find_element(By.CSS_SELECTOR, "p[class='css-10b0gli er34gjf0']")

        # Oczekuj na pojawienie się elementu yersOfOfferCarString
        yersOfOfferCarString = driverElement.find_element(By.CSS_SELECTOR, "div[class='css-efx9z5']")

        # Oczekuj na pojawienie się elementu linkToOfferElement
        linkToOfferElement = driverElement.find_element(By.CSS_SELECTOR, "a[class='css-rc5s2u']")

        # Oczekuj na pojawienie się elementu titleOfferCarString
        titleOfferCarString = driverElement.find_element(By.CSS_SELECTOR, "h6[class='css-16v5mdi er34gjf0']")
        # Pobierz link do oferty
        linkToOfferString = linkToOfferElement.get_attribute("href")
        # Wyświetl tekst elementów
        whitoutEnterPriceString = priceElement.text.replace('\n', '')
        splitDateAndPlaceElementString = re.split("-", dataDateAndPlaceElement.text)
        splitYearsAndDistanceElementString = re.split("-", yersOfOfferCarString.text)
        print("Data and Place:", dataDateAndPlaceElement.text)
        print("Price:", priceElement.text)
        print("Years of Offer Car:", yersOfOfferCarString.text)
        print("Link to Offer:", linkToOfferString)
        print("Title of Offer Car:", titleOfferCarString.text)
        print(titleOfferCarString.text)
        print(linkToOfferString)
        dictCarElement = {
            "tytul": titleOfferCarString.text,
            "cena": whitoutEnterPriceString,
            "miejscowosc": splitDateAndPlaceElementString[0],
            "dataAdd": splitDateAndPlaceElementString[1],
            "yearOfProduction": splitYearsAndDistanceElementString[0],
            "distance": splitYearsAndDistanceElementString[1],
            "linkToOffer": linkToOfferString,
        }
        dictCarsElementList.append(dictCarElement)
        print(whitoutEnterPriceString)
        print(splitDateAndPlaceElementString[1])
        print(yersOfOfferCarString.text)
        print(splitYearsAndDistanceElementString)




    def testOlxrCarScrapperByTheNewOnePage(self):
        urlWithFilter = "https://www.olx.pl/motoryzacja/samochody/?search%5Border%5D=created_at:desc"
        self.driver.get(urlWithFilter)
        time.sleep(5.4)
        buttonAcept = self.driver.find_element(By.ID, 'onetrust-accept-btn-handler')
        print(buttonAcept)
        buttonAcept.click()
        time.sleep(4.5)
        all_products_reserche_car = self.driver.find_elements(By.CLASS_NAME, 'css-1sw7q4x')
        print(f"Number of products car element : {len(all_products_reserche_car)}")
        carCardsList = self.driver.find_elements(By.CLASS_NAME, "css-1sw7q4x")
        dictCarsElementList = []
        sum_number_page = self.driver.find_elements(By.CSS_SELECTOR, "li[data-testid='pagination-list-item']")
        integerSumPage = int(sum_number_page[len(sum_number_page) - 1].text)
        # self.printUrlWebsite()
        # css-pyu9k9 klasa   pagination-forward
        # css-pyu9k9
        print("tyle jest sum stron "+str(integerSumPage))
        for x in range(integerSumPage):
            time.sleep(2.5)
            print("\n jestem na stronie  "+ self.driver.current_url+'\n')
            carCardsList = self.driver.find_elements(By.CLASS_NAME, "css-1sw7q4x")
            for elementIt in range(len(carCardsList)):
                element = carCardsList[elementIt]
                try:
                    self.findDetalELementScrappScript(element, dictCarsElementList)
                except NoSuchElementException:
                    continue
                except TimeoutException :
                    print("is TimeoutException")
                    time.sleep(1)
                    continue
                except StaleElementReferenceException:
                    continue
                    # self.driver.refresh()
                    # time.sleep(1)
                    # self.findDetalELementScrappScript(element,dictCarsElementList)
                except NoSuchWindowException:
                    self.driver.get("https://www.olx.pl/motoryzacja/samochody/?page=" + str(
                        x + 1) + "&search%5Border%5D=created_at%3Adesc")
                    time.sleep(2.5)
            self.driver.get("https://www.olx.pl/motoryzacja/samochody/?page="+str(x+1)+"&search%5Border%5D=created_at%3Adesc")
        self.createCSVResultScrapingTest(dictCarsElementList,["tytul","cena","miejscowosc","dataAdd","yearOfProduction","distance","linkToOffer"])
        print("po wykonaniu petli")



    def beforeStepsOnePageOlxCarScrapp(self,urlWitHFilterOlx="https://www.olx.pl/motoryzacja/samochody/?search%5Border%5D=created_at:desc"):
        self.driver.get(urlWitHFilterOlx)
        time.sleep(5.4)
        try:
            buttonAcept = WebDriverWait(self.driver, 5).until( EC.presence_of_element_located((By.ID, 'onetrust-accept-btn-handler')))
            # print(buttonAcept)
            buttonAcept.click()
        except TimeoutException:
                print("is TimeoutException")
                time.sleep(2)
                self.driver.refresh()
                buttonAcept = WebDriverWait(self.driver, 7).until(
                    EC.presence_of_element_located((By.ID, 'onetrust-accept-btn-handler')))
                buttonAcept.click()
        except NoSuchElementException:
            print("NoSuchElementException")
            self.driver.refresh()
            buttonAcept = WebDriverWait(self.driver, 7).until(
                EC.presence_of_element_located((By.ID, 'onetrust-accept-btn-handler')))
            buttonAcept.click()


    def scrapeOnePageOlxCarScrapp(self,url):
        self.driver.get(url)
        time.sleep(3)
        all_products_reserche_car = self.driver.find_elements(By.CLASS_NAME, 'css-1sw7q4x')
        # print(f"Number of products car element : {len(all_products_reserche_car)}")
        carCardsList = self.driver.find_elements(By.CLASS_NAME, "css-1sw7q4x")
        dictCarsElementList = []
        sum_number_page = self.driver.find_elements(By.CSS_SELECTOR, "li[data-testid='pagination-list-item']")
        # print("znalazlem ilosc stron ponizej")
        integerSumPage = int(sum_number_page[len(sum_number_page) - 1].text)
        for elementIt in range(len(carCardsList)):
            element = carCardsList[elementIt]
            try:
                # Oczekuj na pojawienie się elementu dataDateAndPlaceElement
                element.find_element()
                dataDateAndPlaceElement = WebDriverWait(self.driver, 5).until(
                    element.find_element(By.CSS_SELECTOR, "p[class='css-veheph er34gjf0']")
                )

                # Oczekuj na pojawienie się elementu priceElement
                priceElement = WebDriverWait(self.driver, 5).until(
                    element.find_element(By.CSS_SELECTOR, "p[class='css-10b0gli er34gjf0']")
                )

                # Oczekuj na pojawienie się elementu yersOfOfferCarString
                yersOfOfferCarString = WebDriverWait(self.driver, 5).until(
                    element.find_element(By.CSS_SELECTOR, "div[class='css-efx9z5']")
                )

                # Oczekuj na pojawienie się elementu linkToOfferElement
                linkToOfferElement = WebDriverWait(self.driver, 5).until(
                    element.find_element((By.CSS_SELECTOR, "a[class='css-rc5s2u']"))
                )

                # Oczekuj na pojawienie się elementu titleOfferCarString
                titleOfferCarString = WebDriverWait(self.driver, 5).until(
                    element.find_element((By.CSS_SELECTOR, "a[class='css-rc5s2u']") )
                )

                # Pobierz link do oferty




                linkToOfferString = linkToOfferElement.get_attribute("href")
                whitoutEnterPriceString = priceElement.text.replace('\n', '')
                splitDateAndPlaceElementString = re.split("-", dataDateAndPlaceElement.text)
                splitYearsAndDistanceElementString = re.split("-", yersOfOfferCarString.text)
                dictCarElement = {
                    "tytul": titleOfferCarString.text,
                    "cena": whitoutEnterPriceString,
                    "miejscowosc": splitDateAndPlaceElementString[0],
                    "dataAdd": splitDateAndPlaceElementString[1],
                    "yearOfProduction": splitYearsAndDistanceElementString[0],
                    "distance": splitYearsAndDistanceElementString[1],
                    "linkToOffer": linkToOfferString,
                }
                print(str(dictCarElement.keys())+" " +str(dictCarElement.values() ))
                dictCarsElementList.append(dictCarElement)
            except NoSuchElementException:
                continue
            except TimeoutException:
                print("is TimeoutException")
                time.sleep(1)
                continue
        self.createCSVResultScrapingTest(dictCarsElementList,['tytul', 'cena', 'miejscowosc', 'dataAdd', 'yearOfProduction', 'distance', 'linkToOffer'])

    # Podaje dane kluczowe np cena, rok, data  dodania(do 7 dni wstecz), przebieg od - do , marka, model i codziennie  dostaje raport na temat nowych ofert dodanych
    def printUrlWebsite(self):
        print(self.driver.current_url)


    def getLinksAdressOlxScraping(self):
        try:
            if(self.driver.current_url.find("olx")) :
                listUrl=[]
                intHowManyPage=self.getNumberSiteOlxOferrPage()
                for x in range(intHowManyPage):
                    listUrl.append("https://www.olx.pl/motoryzacja/samochody/?page=" + str(x + 1) + "&search%5Border%5D=created_at%3Adesc")
                return listUrl
            else:
                print("Please set up driver on olxwebsite")
        except InvalidSessionIdException:
            print("Occurs if the given session id is not in "
                  "the list of active sessions, meaning the session either does not "
                  "exist or that it’s not active.")


    def effectiveScrapUsingThreadOLxCar(self):
        # Lista URL-ów do zescrapowania
        # scrapeOnePageOlxCarScrapp
        self.printUrlWebsite()
        urls = self.getLinksAdressOlxScraping()
        # Tworzenie wątków dla każdego URL-a
        threads = []
        for url in urls:
            thread = threading.Thread(target=self.scrapeOnePageOlxCarScrapp(url), args=(url,))
            threads.append(thread)
            thread.start()

        # Czekanie na zakończenie wszystkich wątków
        for thread in threads:
            thread.join()

        print("Scraping zakończony.")



    def getResultScrapMeraToDict(self, textPhrasesToSerche):
        self.testMeraSearche(textPhrasesToSerche)
        time.sleep(2.4)
        element_more_pages = self.driver.find_elements(By.CLASS_NAME, "pagination__element")
        print(
            f"this is values elemeont_more_page : {element_more_pages}  +\n wielkosc tablicy : {len(element_more_pages)} ")
        list_element_more_page = []

        list_all_product = []
        dateTimeTest = datetime.datetime.now()
        all_products_reserche = self.driver.find_elements(By.CLASS_NAME, "product")
        print(f"I found {textPhrasesToSerche}  : {len(all_products_reserche)}")

        try:
            for product in all_products_reserche:
                price_elm = product.find_element(By.CLASS_NAME, 'price')
                name_elm = product.find_element(By.CLASS_NAME, 'product__name')
                price = price_elm.text
                name = name_elm.text
                url = name_elm.get_attribute('href')
                print("-------")
                print(name)
                print(url)
                # print(price)
                print("-----")
                list_all_product.append({'name': name, 'price': price, 'url_website': url, 'dateTime': dateTimeTest})
            print(list_all_product)
            with open('/Users/dawidlefuk/Desktop/udemy/Selenium web drive/SeleniumPyCrashCourse/employee_file2.csv',
                      mode='w') as csv_file:
                fieldnames = ['name', 'price', 'url_website', 'dateTime']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for product in list_all_product:
                    writer.writerow(product)

        except selenium.common.exceptions.TimeoutException:
            print("Masz slaby internet ")


        # first click on button zaloguj  (button for login class=cntBtn or class = myOffersBtn showUserName, inputLogin id=inpLogin, input password  id=inpPassword, button login  class = theButton
        # after login, class=title offerLink, class price_value, class = row odd, class row even
        #
        def prepareDataFromMyAcountOfferSprzedajemy(self, login, password):
            self.driver.get("https://sprzedajemy.pl/")
            time.sleep(2.4)
            buttonAcceptCooke = self.driver.find_element(By.ID, "didomi-notice-agree-button")
            buttonAcceptCooke.click()
            buttonLogin = self.driver.find_element(By.CLASS_NAME, "cntBtn")
            buttonLogin.click()
            inputLogin = self.driver.find_element(By.ID, "inpLogin")
            inputPassword = self.driver.find_element(By.ID, "inpPassword")
            buttonLoginNext = self.driver.find_element(By.CLASS_NAME, "theButton")

            inputLogin.send_keys(login)
            inputPassword.send_keys(password)
            buttonLoginNext.click()
            mainPath = '/Users/dawidlefuk/Desktop/udemy/Selenium web drive/SeleniumPyCrashCourse/arkusz_with_product'
            countPage = 0
            time.sleep(2.4)
            elementPageList = self.driver.find_elements(By.PARTIAL_LINK_TEXT, "Twoje-Oferty")
            print(f"ilosc elementow {len(elementPageList)}")

            while (countPage < 6):
                print("****************************")
                print("I go to next pagee ")
                print("*****************************")
                listDictToSave = self.getDictionaryDataOfferAccountPage()
                # self.createCSVWithDataOffer(listDictToSave, mainPath+f"_data_{countPage}.csv")
                self.appendCSVWithDataOffer(listDictToSave, ['title_offer', 'link_to_offer', 'price_offer', 'id_to_offer'],
                                            mainPath + f"_data_{countPage}.csv")
                self.moveToNextPageAccountSprzedajemy()
                countPage = countPage + 1


        def getDictionaryDataOfferAccountPage(self):
            try:
                time.sleep(2.4)
                listEllementAdd = self.driver.find_elements(By.CSS_SELECTOR, 'tr[class="row odd"]')
                listEllementEven = self.driver.find_elements(By.CSS_SELECTOR, 'tr[class="row even"]')
                allElementList = []
                allElementList.extend(listEllementAdd)
                allElementList.extend(listEllementEven)
                # print(str(len(allOfferOnItem)))
                print('-------------')
                print(str(len(listEllementAdd)))
                print(str(len(listEllementEven)))
                print(str(len(allElementList)))
                print('-------------')
                listDictWithData = []
                print("Ponize lista produktow")
                for element in allElementList:
                    oneRowOfferTitle = element.find_element(By.CSS_SELECTOR, 'a[class="title offerLink"]')
                    oneRowOfferPriceValue = element.find_element(By.CSS_SELECTOR, 'span[class="price_value"]')
                    oneRowOfferIdOffer = element.find_element(By.CSS_SELECTOR, 'div[class="offerNumber"]')
                    oneRowOfferTitleUrl = oneRowOfferTitle.get_attribute('href')
                    print("**************")
                    print(oneRowOfferTitle.text)
                    print(oneRowOfferTitleUrl)
                    print(oneRowOfferPriceValue.text)
                    print(oneRowOfferIdOffer.text)
                    print("**********************")
                    listDictWithData.append({"title_offer": oneRowOfferTitle.text, "link_to_offer": oneRowOfferTitleUrl,
                                             "price_offer": oneRowOfferPriceValue.text, "id_to_offer": oneRowOfferIdOffer.text})
                return listDictWithData


            except NoSuchElementException:
                print("I dont found  offert on this page  ! Check code or connection !")


    def appendCSVWithDataOffer(self, listDictWithDateTosave, listStringTitleCOlumn,
                               pathFile="/Users/dawidlefuk/Desktop/udemy/Selenium web drive/SeleniumPyCrashCourse/employee_file33.csv"):
        time.sleep(2.4)
        with open(pathFile, mode='a') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=listStringTitleCOlumn)
            writer.writeheader()
            for row in listDictWithDateTosave:
                writer.writerow(row)
            time.sleep(1.0)
            print("I append to table  table")


    def createCSVResultScrapingTest(self, listDictWithDateTosave, listStringTitleColumn,
                    pathToSaveCSV='/Users/dawidlefuk/Desktop/udemy/Selenium web drive/SeleniumPyCrashCourse/car_file22.csv'):
        with open(pathToSaveCSV,
                  mode='w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=listStringTitleColumn)
            writer.writeheader()
            writer.writerows(listDictWithDateTosave)
            print("I create table ")


    # Function wchih coppy data from allegro offer
    def copyDataOfferFromAlleggro(self):
        pass


    # FUnction login class="mlc-masthead__main-nav__toggler",
    def loginToallegroLokalnie(self):
        self.driver.get("https://allegrolokalnie.pl/")
        time.sleep(2.0)
        elementCookes = self.driver.find_element(By.ID, "cookies_confirm")
        elementCookes.click()
        time.sleep(1)
        elementLogin = self.driver.find_element(By.CLASS_NAME, "mlc-masthead__main-nav__toggler")
        elementLogin.click()
        time.sleep(1)
        elemeentZalogujKontemAllegro = self.driver.find_element(By.CSS_SELECTOR, 'a[class="mlc-dropdown-menu__dropdown-link"]')
        elemeentZalogujKontemAllegro.click()
        time.sleep(1)
        elementAgree = self.driver.find_element(By.CSS_SELECTOR,'button[class="mgn2_14 mp0t_0a m9qz_yp mp7g_oh mse2_40 mqu1_40 mtsp_ib mli8_k4 mp4t_0 munh_0 m911_5r mefy_5r mnyp_5r mdwl_5r msbw_2 mldj_2 mtag_2 mm2b_2 mqvr_2 msa3_z4 mqen_m6 meqh_en m0qj_5r mh36_16 mvrt_16 mg9e_0 mj7a_0 mjir_sv m2ha_2 m8qd_qh mjt1_n2 b1vf8 mgmw_9u msts_enp mrmn_qo mrhf_u8 m31c_kb m0ux_fp bnpxh mjru_k4 _158e2_4-oWM m3h2_0 m3h2_16_s mryx_24 mryx_0_s mryx_24_x m7er_0k"')
        elementAgree.click()


    # @TODO: make function to reade csv with optimalization(check product exist )
    # TODO: make function coppy on csv  description title witch sprzedajemy
    # TODO: make function coppy on csv  description title with allegro

    def moveToNextPageAccountSprzedajemy(self):
        try:
            time.sleep(2.0)
            nextButton = self.driver.find_element(By.CLASS_NAME, "next")
            if (nextButton.is_enabled()):
                nextButton.click()
                return True
            else:
                return False
        except NoSuchElementException:
            print("I dont found  offert on this page  ! Check code or connection !")
            return False



test1 = FactoryPatternTestScrape()
test1.beforeMethod()
test1.driver.get("https://www.olx.pl/motoryzacja/samochody/?view=list")
linkTable=test1.getLinksAdressOlxScraping()
# test1.effectiveScrapUsingThreadOLxCar()
print(linkTable)
start_time = time.time()
test1.testOlxrCarScrapperByTheNewOnePage()
test1.printUrlWebsite()
end_time = time.time()
execution_time = end_time - start_time

