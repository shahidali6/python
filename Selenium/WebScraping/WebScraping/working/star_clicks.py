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

def check_error_strings(website_string):
    list_of_pagenotopen_strings = ['ERR_TUNNEL_CONNECTION_FAILED',
                                   'This site can’t be reached',
                                   'Access Denied',
                                   'ERR_NETWORK_CHANGED',
                                   'Your connection was interrupted']
    for string in list_of_pagenotopen_strings:
        if string in website_string:
            return True
    return False

file_operation = csv_operations()

listofproxies = file_operation.read_txt_to_list('new_proxies')

ad_links = ['http://simplehtmllink.s3-website.me-south-1.amazonaws.com', 
            'http://ppcwebsite.weebly.com']

last_found_ip = ''
loop_counter = 0
loop_limit = 100
#https://piprogramming.org/articles/How-to-make-Selenium-undetectable-and-stealth--7-Ways-to-hide-your-Bot-Automation-from-Detection-0000000017.html
while loop_counter < loop_limit:
    one_proxy = random.choice(listofproxies)
    delay = 0
    proxy = Proxy({
        'proxyType': ProxyType.MANUAL,
        'httpProxy': one_proxy,
        'sslProxy': one_proxy,
        'noProxy': ''})
    capabilities = webdriver.DesiredCapabilities.CHROME
    proxy.add_to_capabilities(capabilities)

    #Open Browser
    option = webdriver.ChromeOptions()
    #Removes navigator.webdriver flag
    #For ChromeDriver version 79.0.3945.16 or over
    option.add_argument('--disable-blink-features=AutomationControlled')

    user_agent_obj = user_agent()
    chrome_user_agent = ''

    while chrome_user_agent == '':
        agent = user_agent_obj.random_user_agent()
        if 'chrome' in agent.lower(): 
            chrome_user_agent = 'user-agent='+agent
            del user_agent_obj
    random_width = random.randint(600, 1300)
    random_height = random.randint(500, 1000)
    option.add_argument(f"window-size={random_width},{random_height}")
    option.add_argument(chrome_user_agent)

    driver = webdriver.Chrome(executable_path='chromedriver.exe',options=option, desired_capabilities=capabilities)
    #driver.implicitly_wait(60)
    #Remove navigator.webdriver Flag using JavaScript
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    #driver = webdriver.Chrome(desired_capabilities=capabilities)
    #try:
    #    delay = 2
    #    driver.get("https://ip.me/")
    #    time.sleep(delay)
    #    driver.get("https://httpbin.org/ip")
    #    time.sleep(delay)
    #    current_ip_raw = driver.find_element_by_xpath("/html/body").text
    #    current_ip = extract_ip(current_ip_raw)
    #    print('Current IP: '+current_ip)    
    #except :
    #    pass
    
    try:
        driver.get(random.choice(ad_links))
        driver.find_element_by_css_selector('tr td font a').click()
        delay = 10
        time.sleep(delay)

        if check_error_strings(driver.page_source):
            delay = 0
        else:
            driver.implicitly_wait(60)
            delay = random.randint(10, 30)
            loop_counter = loop_counter + 1
        time.sleep(delay)
    except :
        pass
    driver.close()
