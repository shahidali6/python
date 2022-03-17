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
import time

from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import os

for x in range(12):
    #https://stackoverflow.com/questions/53942553/how-to-connect-to-tor-browser-using-python
    #torexe = os.popen(r'C:\Users\msaddique\Desktop\TorBrowser\Browser\TorBrowser\Tor\tor.exe')
    #profile = FirefoxProfile(r'C:\Users\msaddique\Desktop\TorBrowser\Browser\TorBrowser\Data\Browser\profile.default')
    torexe = os.popen(r'D:\TorBrowser\Browser\TorBrowser\Tor\tor.exe')
    profile = FirefoxProfile(r'D:\TorBrowser\Browser\TorBrowser\Data\Browser\profile.default')
    profile.set_preference('network.proxy.type', 1)
    profile.set_preference('network.proxy.socks', '127.0.0.1')
    profile.set_preference('network.proxy.socks_port', 9050)
    profile.set_preference("network.proxy.socks_remote_dns", False)
    profile.update_preferences()
    driver = webdriver.Firefox(firefox_profile= profile, executable_path='geckodriver.exe')
    #driver.get("http://check.torproject.org")
    #driver.get("https://whatismyipaddress.com/")
    driver.get("https://httpbin.org/ip")
    #driver.get("http://ppcwebsite.weebly.com/")
    #time.sleep(random.randint(5, 15))
    driver.get("http://simplehtmllink.s3-website.me-south-1.amazonaws.com/")
    time.sleep(5)
    driver.find_element_by_css_selector('tr td font a').click()
    #driver.find_elements_by_xpath('//*[@id="table16"]/tbody/tr[1]/td/font/a').click()
    time.sleep(random.randint(6, 18))
    #driver.get("http://check.torproject.org")
    #time.sleep(random.randint(3, 6))
    driver.close()






binary = FirefoxBinary(r"C:\Users\msaddique\Desktop\TorBrowser\Browser\TorBrowser\Tor\tor.exe")
profile = FirefoxProfile(r"C:\Users\msaddique\Desktop\TorBrowser\Browser\TorBrowser\Data\Browser\profile.default")

# Configured profile settings.

proxyIP = "127.0.0.1"
proxyPort = 9050

proxy_settings = {"network.proxy.type":1,
    "network.proxy.socks": proxyIP,
    "network.proxy.socks_port": proxyPort,
    "network.proxy.socks_remote_dns": False,
}
driver = webdriver.Firefox(firefox_binary=binary,proxy=proxy_settings)

def interactWithSite(driver):

    driver.get("https://whatismyipaddress.com/")    
    #driver.get("https://www.google.com")    
    driver.save_screenshot("screenshot.png")

interactWithSite(driver)





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
