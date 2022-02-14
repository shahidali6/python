
# Tutorial link: https://realpython.com/beautiful-soup-web-scraper-python/
# XPATH tutorial reference added https://www.geeksforgeeks.org/how-to-use-xpath-with-beautifulsoup/
import requests
from bs4 import BeautifulSoup
from lxml import etree
import csv

URL = "https://www.olx.com.pk/lahore_g4060673"
page = requests.get(URL)

print(page.text)

soup = BeautifulSoup(page.content, "html.parser")

#results = soup.find(id="ResultsContainer")
results = soup.find(class_="ba608fb8")
print(results.prettify())

job_elements = results.find_all("div", class_="a52608cc")

print("=========================================================")

status = "No element found"

myList = [];


for job_element in job_elements:
    title_element = job_element.find("div", class_="a5112ca8")
    company_element = job_element.find("div", class_="_52497c97")
    location_element = job_element.find("span", class_="_424bf2a8")

    innerList = []
    try:
        print(title_element.text.strip())
        innerList.append(title_element.text.strip())
    except :
        print(status)
        innerList.append(status)
    try:
        print(company_element.text.strip())
        innerList.append(company_element.text.strip())
    except :
        print(status)
        innerList.append(status)
    try:
        print(location_element.text.strip())
        innerList.append(location_element.text.strip())
    except :
        print(status)
        innerList.append(status)
    
    print("--------Next---------")
    myList.append(innerList)

print("=========================================================")

# open the file in the write mode
f = open('csv_file.csv', 'w', encoding='UTF8')

# create the csv writer
writer = csv.writer(f)

# write a row to the csv file
for item in myList:
    writer.writerow(item)

# close the file
f.close()



