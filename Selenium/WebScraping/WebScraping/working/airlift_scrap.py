
# Tutorial link: https://realpython.com/beautiful-soup-web-scraper-python/
# XPATH tutorial reference added https://www.geeksforgeeks.org/how-to-use-xpath-with-beautifulsoup/
# Very useful tutorial link https://www.dataquest.io/blog/web-scraping-beautifulsoup/
import requests
from bs4 import BeautifulSoup
import csv
import mysql.connector
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from common.file.csv_operations import csv_operations
#for cookies saving and read back
import pickle
#for wait
import time
   
#Lahore: "lahore_g4060673"
#baseURL = "https://www.olx.com.pk"
#URL = baseURL+ "/lahore_g4060673"
baseURL = "https://www.airliftexpress.com"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(baseURL)

cookies = pickle.load(open("airlift_nekapura.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
file_operat = csv_operations()
driver.get(baseURL)

#driver.get('https://www.airliftexpress.com/product-category/promotions?page=50')
driver.get('https://www.airliftexpress.com/product-category/promotions')

time.sleep(5)

soup = BeautifulSoup(driver.page_source, 'html.parser')

all_products = soup.findAll('div', class_='product-card ng-star-inserted')

for product in all_products:
    name = product.find('p', class_='pc-title ant-typography ant-typography-ellipsis ant-typography-ellipsis-multiple-line').text
    price = product.find('div', class_='pc-cost ng-star-inserted').text
    image = product.find('img', class_='pc-img').attrs['src']
    coin = product.find('div', class_='pc-rewards ng-star-inserted').text
    try:
        orignal_price = product.find('div', class_='pc-p-old ng-star-inserted').text
    except :
        orignal_price = '0'
    try:
        discount_percentage = product.find('div', class_='pc-tag ng-star-inserted').text
    except :
        discount_percentage = '0'
    try:
        product_avalible = product.find('button', class_='pc-add-btn ant-btn ant-btn-dangerous ant-btn-block ng-star-inserted').text
    except :
        product_avalible = 'Out of Stock'

    print(name)
    print(price)
    print(image)
    print(coin)
    print(orignal_price)
    print(discount_percentage)
    print(product_avalible)
    print('-----------------------------------------------')

status = file_operat.save_webpage_source('promotions.html',driver.page_source)


#identify text box
countryXpath = "//*[@id=\"cdk-overlay-0\"]/nz-modal-container/div/div/div/ecp-update-delivery-location/ecp-lazy-google-map-wrapper/div/div[2]/form/div/div/div[1]/nz-form-item/nz-form-control/div/div/nz-select/nz-select-top-control/nz-select-search/input"
getElement = driver.find_element_by_xpath(countryXpath)
#send input
getElement.send_keys("Pakistan")
getElement.send_keys(Keys.ARROW_DOWN)
#send keyboard input
getElement.send_keys(Keys.RETURN)
getElement.send_keys(Keys.TAB)
cityxPath = "//*[@id=\"cdk-overlay-0\"]/nz-modal-container/div/div/div/ecp-update-delivery-location/ecp-lazy-google-map-wrapper/div/div[2]/form/div/div/div[2]/nz-form-item/nz-form-control/div/div/nz-select/nz-select-top-control/nz-select-search/input"
getElement = driver.find_element_by_xpath(cityxPath)
getElement.send_keys("Sialkot")
driver.implicitly_wait(0.5)
getElement.send_keys(Keys.ARROW_DOWN)
#send keyboard input
getElement.send_keys(Keys.RETURN)

getElement.send_keys(Keys.TAB)
driver.implicitly_wait(0.5)
areXpath = "//*[@id=\"cdk-overlay-0\"]/nz-modal-container/div/div/div/ecp-update-delivery-location/ecp-lazy-google-map-wrapper/div/div[2]/form/div/div[2]/div[1]/div/nz-form-item/nz-form-control/div/div/nz-select/nz-select-top-control/nz-select-search/input"
getElement = driver.find_element_by_xpath(areXpath)
getElement.send_keys("Neka Pura, Sialkot")
driver.implicitly_wait(1)

area_item_xpath = '//*[@id="cdk-overlay-5"]/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item[1]'
#getElement.send_keys(Keys.ARROW_DOWN)
getElement = driver.find_element_by_xpath(area_item_xpath).click

#save cookies
pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))

#time.sleep(10)
print(driver.get_cookies())
driver.implicitly_wait(1)
getElement.send_keys(Keys.RETURN)
getElement.send_keys(Keys.RETURN)
driver.implicitly_wait(1)

continueButtonxPath = "//*[@id=\"cdk-overlay-0\"]/nz-modal-container/div/div/div/ecp-update-delivery-location/ecp-lazy-google-map-wrapper/div/div[2]/form/div/div[2]/div[3]/button"
getElement = driver.find_element_by_xpath(continueButtonxPath).click()

driver.get('https://www.airliftexpress.com/product-category/promotions')

i = driver.find_element_by_xpath("//*[@id=\"cdk-overlay-0\"]/nz-modal-container/div/div/div/ecp-update-delivery-location/ecp-lazy-google-map-wrapper/div/div[2]/form/div/div/div[1]/nz-form-item/nz-form-control/div/div/nz-select/nz-select-top-control/nz-select-search/input")

s = requests.Session()
# Set correct user agent
selenium_user_agent = driver.execute_script("return navigator.userAgent;")
s.headers.update({"user-agent": selenium_user_agent})

for cookie in driver.get_cookies():
    s.cookies.set(cookie['name'], cookie['value'], domain=cookie['domain'])

response = s.get(baseURL)













interdic = {"address":"Neka Pura, Sialkot, Punjab, Pakistan","name":"Neka Pura, Sialkot, Punjab, Pakistan","placeId":"ChIJcWmQs4fqHjkRRf7DH3jsA7U","latitude":32.4851972,"longitude":74.54779289999999,"city":"Sialkot","country":"Pakistan"}	
cookies_dict = {"warehouseTimeZone": "Asia/Karachi", 
                "deliveryLocation":interdic,
                "cityId":"101",
                "warehouseId":"6268",
                "countryId":"1"
                }


URL = baseURL+ "/product-category/frozen"
page = requests.get(URL,cookies_dict)
curSession = requests.Session() 
getCookies = curSession.get(URL)

#print(page.text)

soup = BeautifulSoup(page.content, "html.parser")

#results = soup.find(id="ResultsContainer")
results = soup.find(class_="ba608fb8")
print(results)

allElements = results.find_all("article", class_="_7e3920c1")

print("=========================================================")

status = "No element found"

myList = [];


for element in allElements:
    innerList = []
    try:
        title = element.find("div", class_="a5112ca8").text.strip()
        print(title)
        innerList.append(title)
    except :
        print(status)
        innerList.append(status)

    try:
        priceStart = element.find("div", class_="_52497c97").span.text.strip().replace("Rs", "").replace(",","").strip()
        priceEnd = ""
        if '|' in priceStart:
            priceSplit = priceStart.split('|')
            if len(priceSplit)>0:
                finalSplit = priceSplit[0].split('-')
                priceStart = finalSplit[0]
                priceEnd = finalSplit[1]
        print(priceStart  +" | "+priceEnd)
        innerList.append(priceStart)
        innerList.append(priceEnd)
    except :
        print("0|0")
        innerList.append(0)
        innerList.append(0)

    try:
        location = element.find("span", class_="_424bf2a8").text.strip()[:-1]
        print(location)
        innerList.append(location)
    except :
        print(status)
        innerList.append(status)
        
    try:
        image = element.find("source").get('srcset').strip()
        print(image)
        innerList.append(image)
    except :
        print(status)
        innerList.append(status)
        
    try:
        link = baseURL+ element.find("div", class_="ee2b0479").a.get('href').strip()
        print(link)
        innerList.append(link)
    except :
        print(status)
        innerList.append(status)
        
    try:
        feature = element.find("span", class_="_151bf64f").text.strip()
        print(feature)
        innerList.append(feature)
    except :
        print(status)
        innerList.append(status)
    
    print(innerList)
    print("--------Next---------")
    if innerList[6] == status:
        myList.append(innerList)

CSV.WriteCSVFile("olx", myList)
InsertDataIntoMySQL(myList)
print("=========================================================")

