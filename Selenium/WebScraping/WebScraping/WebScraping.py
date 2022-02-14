
# Tutorial link: https://realpython.com/beautiful-soup-web-scraper-python/
import requests
from bs4 import BeautifulSoup
from lxml import etree

URL = "https://www.olx.com.pk/lahore_g4060673"
page = requests.get(URL)

print(page.text)

soup = BeautifulSoup(page.content, "html.parser")

#results = soup.find(id="ResultsContainer")
results = soup.find(class_="_7e3920c1")
print(results.prettify())

job_elements = results.find_all("div", class_="a52608cc")

print("=========================================================")

status = "No element found"

for job_element in job_elements:
    title_element = job_element.find("div", class_="a5112ca8")
    company_element = job_element.find("div", class_="_52497c97")
    location_element = job_element.find("span", class_="_424bf2a8")
    try:
        print(title_element.text.strip())
    except :
        print(status)
    try:
        print(company_element.text.strip())
    except :
        print(status)
    try:
        print(location_element.text.strip())
    except :
        print(status)
    
    print("--------Next---------")
print("=========================================================")