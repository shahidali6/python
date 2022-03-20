from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from common.file.csv_operations import csv_operations
# for wait
import time

driver = webdriver.Chrome()
driver.get('https://www.trustpilot.com/')

time.sleep(5)
loading = True

while loading:

    try:
        driver.find_elements_by_class_name('button--block ajax-pager-link').click()
        time.sleep(5)
    except :
        loading = False

soup = BeautifulSoup(driver.page_source, 'html.parser')
names = soup.findAll('div', class_='item clearfix')
print('sdfsdfsdf')