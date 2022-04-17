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