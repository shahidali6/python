import datetime
import time
from bs4 import BeautifulSoup
from bs4.element import SoupStrainer

class grocerapp_operation():
    """The function extract the name and links of the grocerapp.pk website."""
    def extract_categories_links(self, base_url, html_to_extract):
        soup = BeautifulSoup(html_to_extract, "html.parser")

        #Selector used to get the list of categories
        categories_raw = soup.select('main div div div div div div p a b')
        #Selector used to get the lsit of raw links
        links_raw = soup.select('main div div div div div div p a')

        #lists will use to return values
        refine_links = []
        refine_categories = []

        #Populate Categories name list
        for category_text in categories_raw:
            refine_categories.append( category_text.text)

        for link in links_raw:
            link_value = base_url+ link.attrs['href']
            link_text = link.text
            for check_category in refine_categories:
                if check_category == link_text:
                    refine_links.append(link_value)     
        
        print('No Links found') if len(refine_links) == 0 else print('Links found')
        print('No Categories found') if len(refine_categories) == 0 else print('Categories found')

        #Return the lists
        return refine_links, refine_categories

    """The function extract the name and links of the grocerapp.pk website."""
    def extract_product_data(self, base_url, html_to_extract):
        soup = BeautifulSoup(html_to_extract, "html.parser")

        time.sleep(5)
        #Selector used to get the list of categories
        main_product_container = soup.find_all('div', class_='muigrid-root muigrid-container')
        for main in main_product_container:
            #chcch = main.findchildren('div', class_='MuiPaper-root MuiCard-root jss1392 MuiPaper-elevation1 MuiPaper-rounded')
            #product_car = main.find_all('div div div div div')
            #product_car = main.find_all('div', class_='MuiGrid-root jss1372 MuiGrid-item MuiGrid-grid-xs-true')
            product_car = main.find_all('div', class_='muigrid-root muigrid-container muigrid-direction-xs-column muigrid-wrap-xs-nowrap')
            print('I am in!.')
            
        
        product_car = main_product_container.findAll('div', class_='MuiGrid-root MuiGrid-container MuiGrid-direction-xs-column MuiGrid-justify-content-xs-space-between')
        main_product_container1 = soup.findAll('div', class_='MuiGrid-root MuiGrid-container MuiGrid-direction-xs-column MuiGrid-justify-content-xs-space-between')
        product_cards = soup.select('main div div div div div div div div')
        product_cards = soup.select('main > div.jss552 > div.MuiGrid-root.MuiGrid-container > div:nth-child(1) > div > div > div.MuiGrid-root.jss1372.MuiGrid-item.MuiGrid-grid-xs-true > div')
        #Selector used to get the lsit of raw links
        links_raw = soup.select('main div div div div div div p a')

        #lists will use to return values
        refine_links = []
        refine_categories = []

        #Populate Categories name list
        for category_text in categories_raw:
            refine_categories.append( category_text.text)

        for link in links_raw:
            link_value = base_url+ link.attrs['href']
            link_text = link.text
            for check_category in refine_categories:
                if check_category == link_text:
                    refine_links.append(link_value)     
        
        print('No Links found') if len(refine_links) == 0 else print('Links found')
        print('No Categories found') if len(refine_categories) == 0 else print('Categories found')

        #Return the lists
        return refine_links, refine_categories