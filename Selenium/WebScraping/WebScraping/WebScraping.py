
# Tutorial link: https://realpython.com/beautiful-soup-web-scraper-python/
# XPATH tutorial reference added https://www.geeksforgeeks.org/how-to-use-xpath-with-beautifulsoup/
# Very useful tutorial link https://www.dataquest.io/blog/web-scraping-beautifulsoup/
import requests
from bs4 import BeautifulSoup
import csv
import mysql.connector
import datetime

def WriteCSVFile(fileName, myList):
    # open the file in the write mode
    f = open(fileName+datetime.datetime.now().strftime("_%Y%m%d_%H%M")+'.csv', 'w', encoding='UTF8')
    
    # create the csv writer
    writer = csv.writer(f)
    
    # write a row to the csv file
    writer.writerows(myList)

    for item in myList:
        writer.writerow(item)
    
    # close the file
    f.close()
    
def InsertDataIntoMySQL(myList):
    #Insert Data into MySQL 
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="python"
    )
    
    mycursor = mydb.cursor()
    
    for item in myList:
        sql = "INSERT INTO olx (title, pricestart,priceend, location,image,link,feature) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (item)
        mycursor.execute(sql, val)
        mydb.commit()
    
    print(mycursor.rowcount, "record inserted in MytSQL Database.")
#Lahore: "lahore_g4060673"
baseURL = "https://www.olx.com.pk"
URL = baseURL+ "/lahore_g4060673"
page = requests.get(URL)

print(page.text[:100])

soup = BeautifulSoup(page.content, "html.parser")

#results = soup.find(id="ResultsContainer")
results = soup.find(class_="ba608fb8")
print(results.prettify()[:100])

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

WriteCSVFile("olx", myList)
InsertDataIntoMySQL(myList)
print("=========================================================")
