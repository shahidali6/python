
# Tutorial link: https://realpython.com/beautiful-soup-web-scraper-python/
# XPATH tutorial reference added https://www.geeksforgeeks.org/how-to-use-xpath-with-beautifulsoup/
# Very useful tutorial link https://www.dataquest.io/blog/web-scraping-beautifulsoup/
from typing import final
import requests
from bs4 import BeautifulSoup
import csv
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from common.file.csv_operations import csv_operations
#for cookies saving and read back
import pickle
#for wait
import time
from fake_useragent import UserAgent

from common.file.database_operations import database_operations

# function to return avalible and out of stock string
def product_in_stock(args):
    #Expacted value is Add to Cart
    add_to_cart = 'Add to Cart'
    avalible = 'avalible'
    not_avalible = 'out of stock'
    if args.strip() == add_to_cart:
        return avalible 
    else:
        return not_avalible

# function to return pecentage value for example 5 % OFF
def percentage_value_filter(args):
    string_array = args.strip().split(' ')
    if len(string_array) > 1:
        return string_array[0]
    else:
        return string_array[0]

# function to return price value for example Rs 55
def price_value_filter(args):
    string_array = args.strip().split(' ')
    if len(string_array) > 1:
        return string_array[1]
    else:
        return string_array[0]

# function to return coin value for example + 55
def coin_value_filter(args):
    #two spaces defined in HTML file that's reason to split with double spaces
    string_array = args.strip().split('  ')
    if len(string_array) > 1:
        return string_array[1]
    else:
        return string_array[0]

#Lahore: "lahore_g4060673"
#baseURL = "https://www.olx.com.pk"
#URL = baseURL+ "/lahore_g4060673"
baseURL = "https://www.airliftexpress.com"

#Fake user agent tested.
#https://stackoverflow.com/questions/27652543/how-to-use-python-requests-to-fake-a-browser-visit-a-k-a-and-generate-user-agent
fake_user_agent = UserAgent()
for x in range(20):
    print(fake_user_agent.random)   

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(baseURL)
time.sleep(5)

#load saved cookies
cookies = pickle.load(open("airlift_nekapura_sialkot.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
file_operat = csv_operations()
driver.get(baseURL)
time.sleep(5)

#save cookies
#pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))

#driver.get('https://www.airliftexpress.com/product-category/promotions?page=50')
driver.get('https://www.airliftexpress.com/product-category/promotions')

time.sleep(5)

db_operation = database_operations()

SCROLL_PAUSE_TIME = 1
finalbreak = 0
last_product_1 = ''
last_product_2 = ''
external_list = []
while True:
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    location = soup.find('span', class_='dlb-location').text

    all_products = soup.findAll('div', class_='product-card ng-star-inserted')
    if len(all_products) == 0:
        all_products = soup.findAll('div', class_='product-card product-na ng-star-inserted')        

    for product in all_products:
        very_internal = []
        name = product.find('p', class_='pc-title ant-typography ant-typography-ellipsis ant-typography-ellipsis-multiple-line').text.strip()
        price = product.find('div', class_='pc-cost ng-star-inserted').text.strip()
        image = product.find('img', class_='pc-img').attrs['src'].strip()
        link = product.find('a', class_='cursor-pointer').attrs['href'].strip()
        coin = product.find('div', class_='pc-rewards ng-star-inserted').text.strip()
        try:
            orignal_price = product.find('div', class_='pc-p-old ng-star-inserted').text.strip()
        except :
            orignal_price = '0'
        try:
            discount_percentage = product.find('div', class_='pc-tag ng-star-inserted').text.strip()
        except :
            discount_percentage = '0'
        try:
            product_avalible = product.find('button', class_='pc-add-btn ant-btn ant-btn-dangerous ant-btn-block ng-star-inserted').text.strip()
        except :
            product_avalible = 'Out of Stock'

        very_internal.append(name)
        very_internal.append(price_value_filter(price))
        very_internal.append(image)
        very_internal.append(link)
        very_internal.append(coin_value_filter(coin))
        very_internal.append(price_value_filter(orignal_price))
        very_internal.append(percentage_value_filter(discount_percentage))
        very_internal.append(product_in_stock(product_avalible))
        very_internal.append(location)

        #print(name)
        #print(price_value_filter(price))
        #print(image)
        #print(link)
        #print(coin_value_filter(coin))
        #print(price_value_filter(orignal_price))
        #print(percentage_value_filter(discount_percentage))
        #print(product_in_stock(product_avalible))
        #print(location)
        #print('-----------------------------------------------')

        #db_operation.insert_data_into_airlift_table(very_internal)

        last_product_2 = name
        external_list.append(very_internal)

    body = driver.find_element_by_css_selector('body')
    body.click()
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(SCROLL_PAUSE_TIME)

    if last_product_1 == last_product_2:
        finalbreak = finalbreak+1
        if finalbreak > 5:
            break
    else:
        finalbreak = 0
    last_product_1 = last_product_2

csv = csv_operations()
stasts = csv.write_csvfile('airlift_product', external_list)
status = file_operat.save_webpage_source('promotions.html',driver.page_source)