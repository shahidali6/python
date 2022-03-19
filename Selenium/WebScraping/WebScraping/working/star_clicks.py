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
                                   'This site can’t be reached' ]
    for string in list_of_pagenotopen_strings:
        if string in website_string:
            return True
    return False

file_operation = csv_operations()

listofproxies = file_operation.read_txt_to_list('new_proxies')

ad_links = ['http://simplehtmllink.s3-website.me-south-1.amazonaws.com', 
            'http://ppcwebsite.weebly.com']

last_found_ip = ''

for loop in range(100):
    one_proxy = random.choice(listofproxies)
    delay = 0
    proxy = Proxy({
        'proxyType': ProxyType.MANUAL,
        'httpProxy': one_proxy,
        'sslProxy': one_proxy,
        'noProxy': ''})
    accept_insecure_certificate = "'acceptInsecureCerts':'True'"
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

    #for chrome in range(100):
    #    agent = user_agent_obj.random_user_agent()
    #    if 'chrome' in agent.lower(): 
    #        chrome_user_agent = 'user-agent='+agent
    #        break
    #del user_agent_obj

    if chrome_user_agent == '':
        chrome_user_agent = 'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'

    option.add_argument("window-size=1200,650")
    option.add_argument(chrome_user_agent)

    driver = webdriver.Chrome(executable_path='chromedriver.exe',options=option, desired_capabilities=capabilities)

    #Remove navigator.webdriver Flag using JavaScript
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    #driver = webdriver.Chrome(desired_capabilities=capabilities)
    try:
        driver.get("https://httpbin.org/ip")
        delay = 2
        time.sleep(delay)
        current_ip_raw = driver.find_element_by_xpath("/html/body").text
        current_ip = extract_ip(current_ip_raw)
        print('Current IP: '+current_ip)    
    except :
        pass
    
    try:
        driver.get(random.choice(ad_links))
        driver.find_element_by_css_selector('tr td font a').click()
        delay = 5
        time.sleep(delay)

        if check_error_strings(driver.page_source):
            delay = 0
        else:
            delay = random.randint(10, 30)
        time.sleep(delay)
    except :
        pass
    driver.close()


    ##driver.get("http://simplehtmllink.s3-website.me-south-1.amazonaws.com/")
    #time.sleep(5)
    #try:
    #    pass
    #except :
    #    pass
    
    #driver.find_element_by_css_selector('tr td font a').click()

    ##driver.get("https://httpbin.org/ip")

    #time.sleep(25)
    #driver.close()


for one_proxy in listofproxies:
    proxy_url = one_proxy
    proxy = Proxy({
        'proxyType': ProxyType.MANUAL,
        'httpProxy': proxy_url,
        'sslProxy': proxy_url,
        'noProxy': ''})

    capabilities = webdriver.DesiredCapabilities.CHROME
    proxy.add_to_capabilities(capabilities)

    driver = webdriver.Chrome(desired_capabilities=capabilities)
    driver.get("http://simplehtmllink.s3-website.me-south-1.amazonaws.com/")
    driver.get("https://httpbin.org/ip")



    #https://stackoverflow.com/questions/53942553/how-to-connect-to-tor-browser-using-python
    torexe = os.popen(r'C:\Users\msaddique\Desktop\TorBrowser\Browser\TorBrowser\Tor\tor.exe')
    profile = FirefoxProfile(r'C:\Users\msaddique\Desktop\TorBrowser\Browser\TorBrowser\Data\Browser\profile.default')
    #torexe = os.popen(r'D:\TorBrowser\Browser\TorBrowser\Tor\tor.exe')
    #profile = FirefoxProfile(r'D:\TorBrowser\Browser\TorBrowser\Data\Browser\profile.default')
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

ua = user_agent_obj()

loop_counter = 1
#use request for star-clicks impression
for one_proxy in range(impressions):
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
