from selenium.webdriver.common import desired_capabilities
from common.beautifulsoup_operations import beautifulsoup_operations
from common.file.csv_operations import csv_operations
from useragent import user_agent
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import os

def extract_ip(body_text):
    raw_string = body_text.split('"')
    found_ip = 'No IP found'
    if len(raw_string) > 4:
        found_ip = raw_string[3]
        return found_ip
    if len(raw_string) > 2:
        found_ip = raw_string[1]
        return found_ip
    return found_ip

last_found_ip = ''
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

    #https://discuss.dizzycoding.com/open-tor-browser-with-selenium/
    #js can be used to reveal your true i.p.
    #profile.set_preference( "javascript.enabled", False )

    #get a huge speed increase by not downloading images
    profile.set_preference( "permissions.default.image", 2 )    
    profile.update_preferences()
    driver = webdriver.Firefox(firefox_profile= profile, executable_path='geckodriver.exe')
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    #driver.get("http://check.torproject.org")
    #driver.get("https://whatismyipaddress.com/")
    driver.get("https://httpbin.org/ip")
    time.sleep(2)
    #current_ip = driver.find_elements_by_css_selector('body pre')
    #specificly for Tor Browser
    current_ip_raw = driver.find_element_by_xpath("/html/body").text
    current_ip = extract_ip(current_ip_raw)

    #current_ip = driver.find_element_by_xpath("/html/body/pre")
    print('Current IP: '+current_ip)


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