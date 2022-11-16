import time

import timeunit
from selenium import webdriver
from selenium.webdriver.common.by import By

##
# This script scraping price  about website 
####



driver = webdriver.Chrome(executable_path='/Users/dawidlefuk/Desktop/selenium/webdriver/chrome/chromedriver')
driver.implicitly_wait(5)
driver.set_page_load_timeout(15)
url = 'https://mera.eu'
driver.get(url)
searcher = driver.find_element(By.CLASS_NAME, 'menu_search__input')
searcher.send_keys("miska wc")
button_search = driver.find_element(By.CLASS_NAME,'menu_search__submit')
button_search.click()



# all_products = driver.find_elements(By.CLASS_NAME, 'product-type-simple')
# print(f"Number of products: {len(all_products)}")
#
# all_product_an_price = []
# for product in all_products:
#     price_elm = product.find_element(By.CSS_SELECTOR, 'span.amount')
#     price = price_elm.text
#
#     name_elm = product.find_element(By.CSS_SELECTOR, 'h2.woocommerce-loop-product__title')
#     name = name_elm.text
#     print(price)
#     print(name)
#     all_product_an_price.append({'name': name, 'price': price})
#
# print(len(all_product_an_price))
# print(all_product_an_price)



