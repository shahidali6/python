# Tutorial link: https://realpython.com/beautiful-soup-web-scraper-python/
# XPATH tutorial reference added https://www.geeksforgeeks.org/how-to-use-xpath-with-beautifulsoup/
# Very useful tutorial link https://www.dataquest.io/blog/web-scraping-beautifulsoup/
#https://stackoverflow.com/questions/55689701/how-to-use-tor-with-chrome-browser-through-selenium
from typing import final
import requests
from bs4 import BeautifulSoup
import csv
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from common.file.csv_operations import csv_operations
# for cookies saving and read back
import pickle
# for wait
import time
import mysql.connector
from common.database.database_operations import database_operations
#importing the os module
import os
from common.file.file_operations import fileOperations
from urllib.parse import urlparse
#Local imports
from working.grocerapp import grocerapp_operation

# function to return available and out of stock product
def product_in_stock(args):
    # Expacted value is Add to Cart
    add_to_cart = 'Add to Cart'
    avalible = 'available'
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
    # two spaces defined in HTML file that's reason to split with double spaces
    string_array = args.strip().split('  ')
    if len(string_array) > 1:
        return string_array[1]
    else:
        return string_array[0]

### Unique list return all duplicate values removed.
def unique_listoflist(list_data):
    unique_data = [list(x) for x in set(tuple(x) for x in list_data)]
    return unique_data

# extract links and categories from pages source
def airlift_links_categories(list_raw):
    all_links = []
    all_link_categories = []
    for link in list_raw:
        full_link = base_url + link.attrs['href']
        category_name = link.text
        all_links.append(full_link)
        all_link_categories.append(category_name)
        print(full_link + ' [' + category_name +']')
        return all_links, all_link_categories

base_url = "https://grocerapp.pk"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(base_url)
time.sleep(5)
grocer_obj = grocerapp_operation()
links, gategories = grocer_obj.extract_categories_links(base_url, driver.page_source)

for link in links:
    driver.get(link)
    list_product = grocer_obj.extract_product_data(base_url, driver.page_source)



#listOfAllFiles = fileOperations.ListOfFileAndDirectoriesCurrentDirectory()
cookiesfiles = fileOperations.ListFileCurrentDirectory('pkl')

for cookie in cookiesfiles:
    #Lahore: "lahore_g4060673"
    #baseURL = "https://www.olx.com.pk"
    #URL = baseURL+ "/lahore_g4060673"
    base_url = "file://C:/Users/shahid/Downloads/Buy Pakistan Day Sale - _ airliftexpress.com.html"

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(base_url)
    #driver.execute_script("document.body.style.zoom='70%'")
    #time.sleep(5)

    # load saved cookies
    #cookies = pickle.load(open("airlift_nekapura_sialkot.pkl", "rb"))
    cookies = pickle.load(open(cookie, "rb"))
    #for cookie in cookies:
        #driver.add_cookie(cookie)
    file_operat = csv_operations()
    if 'lahore' in cookie:
        base_url = 'https://www.airliftexpress.com/product-category/grocery'
    driver.get(base_url)
    time.sleep(5)
   
    source = urlparse(base_url).hostname

    soup = BeautifulSoup(driver.page_source, "html.parser")

    #all_links = soup.select_one('ecp-app-side-panel aside ecp-category nav ul')
                    #class_='table table-striped table-bordered')
    all_links_raw = soup.select('ecp-category nav ul li a')

    all_links, all_link_categories  = airlift_links_categories(all_links_raw)

    # save cookies
    #pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))

    all_item_list = []
    start_time=time.time()

    loopCounter = 0
    for link in all_links:
        #driver.get(link)
        #driver.execute_script("document.body.style.zoom='zoom 75%'")
        time.sleep(5)
        SCROLL_PAUSE_TIME = 1
        finalbreak = 0
        last_product_1 = ''
        last_product_2 = ''
        external_list = []
        while True:
            soup = BeautifulSoup(driver.page_source, 'html.parser')

            location = soup.find('span', class_='dlb-location').text

            all_master_category = soup.select('ecp-home main ecp-l0-links div div div a')

            all_products = soup.findAll('div', class_='product-card ng-star-inserted')
            if len(all_products) == 0:
                all_products = soup.findAll(
                    'div', class_='product-card product-na ng-star-inserted')
            not_found = 'not found'
            for product in all_products:
                very_internal = []
                try:
                    name = product.find(
                    'p', class_='pc-title ant-typography ant-typography-ellipsis ant-typography-ellipsis-multiple-line').text.strip()
                except:
                    name = not_found
                try:
                    price = product.find(
                    'div', class_='pc-cost ng-star-inserted').text.strip()
                except:
                    price = '-1'
                try:
                    image = product.find('img', class_='pc-img').attrs['src'].strip()
                except:
                    image = not_found
                try:
                    link = base_url + product.find('a', class_='cursor-pointer').attrs['href'].strip()
                except:
                    link = not_found
                try:
                    coin = product.find(
                    'div', class_='pc-rewards ng-star-inserted').text.strip()
                except:
                    coin = '-1'            
                try:
                    orignal_price = product.find(
                        'div', class_='pc-p-old ng-star-inserted').text.strip()
                except:
                    orignal_price = '0'
                try:
                    discount_percentage = product.find(
                        'div', class_='pc-tag ng-star-inserted').text.strip()
                except:
                    discount_percentage = '0'
                try:
                    product_avalible = product.find(
                        'button', class_='pc-add-btn ant-btn ant-btn-dangerous ant-btn-block ng-star-inserted').text.strip()
                except:
                    product_avalible = not_found

                very_internal.append(name)
                very_internal.append(all_link_categories[loopCounter])
                very_internal.append(price_value_filter(price))
                very_internal.append(base_url + image)
                very_internal.append(link)
                very_internal.append(coin_value_filter(coin))
                very_internal.append(price_value_filter(orignal_price))
                very_internal.append(percentage_value_filter(discount_percentage))
                very_internal.append(product_avalible)
                very_internal.append(location)
                very_internal.append(source)

                last_product_2 = name
                external_list.append(very_internal)

            #db_operation.insert_data_into_airlift_table(very_internal)

            body = driver.find_element_by_css_selector('body')
            body.click()
            #body.send_keys(Keys.PAGE_DOWN)
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(SCROLL_PAUSE_TIME)

            if last_product_1 == last_product_2:
                finalbreak = finalbreak+1
                if finalbreak > 5:
                    break
            else:
                finalbreak = 0
            last_product_1 = last_product_2

        total_time_seconds = round(time.time()-start_time,0)
        #external_list.append(total_time_seconds)
        csv = csv_operations()
        #stasts = csv.write_csvfile('airlift_product', external_list)
        #status = file_operat.save_webpage_source('promotions.html', driver.page_source)
        all_item_list.extend(external_list)
        loopCounter +=1

    print(total_time_seconds)
    csv = csv_operations()
    #stasts = csv.write_csvfile('airlift_product_full', all_item_list)

    unique_list = unique_listoflist(all_item_list)

    stasts = csv.write_csvfile('airlift_product_full_unique', unique_list)
    db_operation = database_operations()
    #add dat into local database
    for row in unique_list:
        query = "INSERT INTO airlift (name,category,price,image,link,coin,orignal_price,discount_percentage,product_avalible,location, source) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        host_name="localhost"
        user_name="root"
        password=""
        database="python"
        db_operation.insert_data_into_mysql_table(row, host_name, database, user_name, password, query)
        #insert_data_into_mysql_table(row, host_name, database, user_name, password, query)
        time.sleep(0.01)

    #add dat into aws database
    for row in unique_list:
        query = "INSERT INTO airlift_main (name,category,price,image,link,coin,orignal_price,discount_percentage,product_avalible,location, source) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        host="db-python-webscraping.cpxtybckovvs.us-east-2.rds.amazonaws.com"
        user="dbadmin"
        password="Aesn8POSA2kTzjt1GAk9"
        database="airlift"
        db_operation.insert_data_into_mysql_table(row, host_name, database, user_name, password, query)
        #insert_data_into_mysql_table(row, host, database, user, password, query)
        time.sleep(0.01)
    driver.close()