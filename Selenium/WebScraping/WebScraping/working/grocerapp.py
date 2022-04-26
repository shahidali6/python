import datetime
import time
from bs4 import BeautifulSoup
from bs4.element import SoupStrainer
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.parse import urlparse
from selenium.webdriver.common.by import By

class grocerapp_operation():
    """The function extract the categories and links of the grocerapp.pk website."""
    def extract_categories_links(self, base_url, html_to_extract):
        soup = BeautifulSoup(html_to_extract, "html.parser")

        #Selector used to get the list of categories
        #categories_raw = soup.select('main div div div div div div p a b')
        #Selector used to get the lsit of raw links
        links_raw = soup.select('main div div div div div div p a')

        #lists will use to return values
        refine_links = []
        #refine_categories = []

        #Populate Categories name list
        #for category_text in categories_raw:
        #    refine_categories.append( category_text.text)

        for link in links_raw:
            link_value = base_url+ link.attrs['href']
            link_text = link.text
            for check_category in refine_categories:
                if check_category == link_text:
                    refine_links.append(link_value)     
        
        print('No Links found') if len(refine_links) == 0 else print('Links found')
        #print('No Categories found') if len(refine_categories) == 0 else print('Categories found')

        #Return the lists
        return refine_links#, refine_categories

    """The function extract the name and links of the grocerapp.pk website."""
    def extract_product_data(self, base_url, html_to_extract):
        base_url = "https://grocerapp.pk"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        time.sleep(2)
        grocer_obj = grocerapp_operation()
        productListToReturn = []

        links = self.extract_categories_links(base_url, driver.page_source)

        for link in links:
            driver.get(link)
            body = driver.find_element_by_css_selector('body')
            loopTerminator = True
            loopRetries = 0
            bodyHeight = body.rect['height']
            bodyHeightCheck = ''

            while loopTerminator:
                #body.send_keys(Keys.PAGE_DOWN)
                body.send_keys(Keys.END)
                time.sleep(1)
                bodyHeightCheck = body.rect['height']
                if bodyHeight == bodyHeightCheck:
                    if loopRetries > 10:
                        loopTerminator = False
                    loopRetries += 1
                else:
                    bodyHeight = bodyHeightCheck
                    loopRetries = 0
    
            products_xpath = '/html/body/div[1]/div/main/div[1]/div[3]/div/div/div/div[2]/div'
            main_content = driver.find_elements(by=By.XPATH, value=products_xpath)
            #main_content = driver.find_elements_by_xpath(products_xpath)
            for item in main_content:
                singleListProduct =[]
                name = category = price = image = link = coin = orignal_price = discount_percentage = units = product_avalible = location = source = ''

                category = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/main/div[1]/div[1]/h1').text
                location = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/main/header/div/div[1]/div/div[1]/div/div[2]/div/div/p').text
                #source = url.domin_finder(driver.current_url)
                source = urlparse(driver.current_url).hostname
                link = item.find_element(by=By.TAG_NAME, value='a').get_attribute('href')
                image = item.find_element(by=By.TAG_NAME, value='img').get_attribute('src')
                listProduct = item.text.split('\n')
                if len(listProduct) == 6:
                    name = listProduct[0]
                    units = listProduct[1]
                    price = listProduct[2]
                    orignal_price = listProduct[3]
                    discount_percentage = listProduct[4]
                    product_avalible = listProduct[5]

                if len(listProduct) == 4:
                    name = listProduct[0]
                    units = listProduct[1]
                    price = listProduct[2]
                    product_avalible = listProduct[3]

                singleListProduct.append(name,category, price, image, link, orignal_price, discount_percentage, units, product_avalible, location, source)
                print(name)
                print(category)
                print(price)
                print(image)
                print(link)
                print(orignal_price)
                print(discount_percentage)
                print(units)
                print(product_avalible)
                print(location)
                print(source)
                print('-----------------------------------------')
            productListToReturn.append(singleListProduct)