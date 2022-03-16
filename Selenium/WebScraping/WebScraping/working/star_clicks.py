from selenium.webdriver.common import desired_capabilities
from common.beautifulsoup_operations import beautifulsoup_operations
from common.file.csv_operations import csv_operations
from useragent import user_agent
import random
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.proxy import Proxy, ProxyType

impressions = random.randint(3, 10)

bs = beautifulsoup_operations()
#list_of_proxyies = bs.read_proxies_sslproxies_org()

csv = csv_operations()
#csv.write_list_to_txt('ListofProxy', list_of_proxyies)

#listofips = csv.read_txt_to_list('ListofProxy')
listofips = csv.read_txt_to_list('ListofProxy_working')

ua = user_agent()

loop_counter = 1
#use request for star-clicks impression
for x in range(impressions):
    #proxy = {'https': random.choice(listofips).strip()}
    ##print(ua.random_user_agent())
    ##header = {'User-Agent':str(ua.random_user_agent())
    #user_a = ua.random_user_agent()
    #header = {'User-Agent':user_a}
    #print(str(loop_counter)+ ': '+ user_a)
    ##url = "https://www.hybrid-analysis.com/recent-submissions?filter=file&sort=^timestamp"
    #url = "http://ppcwebsite.weebly.com"
    #htmlContent = requests.get(url, headers=header, proxies=proxy)

    PROXY = random.choice(listofips).strip()

    proxy_obj = Proxy()
    proxy_obj.proxyType = ProxyType.MANUAL
    proxy_obj.http_proxy = PROXY
    proxy_obj.ssl_proxy = PROXY

    capabilitie = webdriver.DesiredCapabilities.CHROME
    proxy_obj.add_to_capabilities(capabilitie)

    chrome = webdriver.Chrome(desired_capabilities=capabilitie)

    #chrome.get('https://whatismyipaddress.com/')
    chrome.get('https://httpbin.org/ip')

    #proxy = Proxy({
    #'proxyType': ProxyType.MANUAL,
    #'httpProxy': PROXY,
    #'sslProxy': PROXY,
    #'noProxy': ''})

    #options = Options()
    #options.proxy = proxy


    #chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--proxy-server=%s' % PROXY)
    #chrome = webdriver.Chrome(chrome_options=chrome_options)
    #chrome.set_page_load_timeout(30)
    ##chrome.get('https://www.whatismyip.com/')
    #chrome.get('https://whatismyipaddress.com/')
    ##chrome.get('https://ppcwebsite.weebly.com')





    #proxy server definition
    prox = random.choice(listofips).strip()
    #configure ChromeOptions class
    chrome_options = WebDriverWait.ChromeOptions()
    #proxy parameter to options
    chrome_options.add_argument('--proxy-server=%s' % prox)
    #options to Chrome()
    driver = webdriver.Chrome(chrome_options= chrome_options)
    driver.implicitly_wait(0.6)
    driver.get('https://www.whatismyip.com/')
    time.sleep(random.randint(5, 15))
    driver.close()



    #driver = webdriver.Chrome()
    #driver.get(url)
    #time.sleep(random.randint(2, 7))
    #loop_counter = loop_counter+1

print("file written!")
