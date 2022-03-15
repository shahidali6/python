import requests
from bs4 import BeautifulSoup
from tkinter import messagebox

class beautifulsoup_operations:
    def read_proxies_sslproxies_org(self):
        try:
            URL = "https://sslproxies.org/"
            page = requests.get(URL)

            if page.status_code != 200:
                print("Error fetching page")
                exit()

            soup = BeautifulSoup(page.content, "html.parser")

            #all_rows = soup.findAll('tr')
            proxy_table = soup.findAll(
                class_='table table-striped table-bordered')

            list_all_proxy = []

            for x in proxy_table[0].contents[1].contents:
                all_td = x.find_all('td')
                ip_and_port = all_td[0].text.strip()+':'+all_td[1].text.strip()
                list_all_proxy.append(ip_and_port)
                print(ip_and_port)
            return list_all_proxy
        except Exception as ex:
            messagebox.showerror("Exception Message", "Exception: "+str(ex))
            return False
