import time
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys

# import namespaces to show error message
# from tkinter import *
from tkinter import messagebox

import requests
from bs4 import BeautifulSoup

class driver_chrome:
    baseURL = "https://www.airliftexpress.com"
    main_driver = ""

    def initiate_driver(self, base_url):
        try:
            driver = webdriver.Chrome()
            driver_options = webdriver.ChromeOptions()
            baseURL = base_url
            driver.get(base_url)
            main_driver = driver
        except Exception as ex:
            messagebox.showerror("Exception Message", "Exception: " + str(ex))

    def find_element_by_xpath_and_send_string_key(self, xpath_value, key_to_send):
        try:
            getElement = main_driver.find_element_by_xpath(xpath_value)
            # send input
            getElement.send_keys(key_to_send)
            getElement.send_keys(Keys.ARROW_DOWN)
            # send keyboard input
            getElement.send_keys(Keys.RETURN)
        except Exception as ex:
            messagebox.showerror("Exception Message", "Exception: " + str(ex))

    def initiate_driver_get_cookies(
        self,
        base_url,
        countryXpath,
        countryText,
        cityxPath,
        cityText,
        areaxPath,
        areaText,
        firstitemDropDown,
        continueButtonxPath,
    ):
        try:
            driver = webdriver.Chrome()
            driver_options = webdriver.ChromeOptions()
            baseURL = base_url
            driver.get(base_url)
            main_driver = driver

            delay = 5

            # identify text box
            getElement = driver.find_element_by_xpath(countryXpath)
            # send input
            getElement.send_keys(countryText)
            #getElement.send_keys(Keys.ARROW_DOWN)
            driver.implicitly_wait(delay)
            # send keyboard input
            getElement.send_keys(Keys.RETURN)
            #getElement.send_keys(Keys.TAB)
            getElement = driver.find_element_by_xpath(cityxPath)
            getElement.send_keys(cityText)
            driver.implicitly_wait(delay)
            #getElement.send_keys(Keys.ARROW_DOWN)
            # send keyboard input
            getElement.send_keys(Keys.RETURN)
            driver.implicitly_wait(delay)
            getElement = driver.find_element_by_xpath(areaxPath)
            getElement.send_keys(areaText)
            driver.implicitly_wait(delay+1)
            # send keyboard input
            getElement.send_keys(Keys.RETURN)
            driver.implicitly_wait(delay+1)

            driver.find_element_by_xpath(firstitemDropDown).click()
            driver.implicitly_wait(delay+1)

            time.sleep(5)
            getElement = driver.find_element_by_xpath(continueButtonxPath).click()
            driver.implicitly_wait(delay+1)

            s = requests.Session()
            # Set correct user agent
            selenium_user_agent = driver.execute_script("return navigator.userAgent;")
            s.headers.update({"user-agent": selenium_user_agent})

            cookkkk = driver.get_cookies()
            
            f = open("receivedCookies.txt", "w")

            for x in cookkkk:
                f.write(str(x))
            f.close()

            cooooookies = {}
            #for cookie in driver.get_cookies():
            #    s.cookies.set(cookie['name'], cookie['value'], domain=cookie['domain'])
            time.sleep(5) #This is the fix

            cookiesItesm = driver.get_cookies()

            requestCookiesList = []

            for cookie in cookiesItesm:
                one_cookie = {}

                for key, value in cookie.items():
                    #test =  cookie[cookie['name']] = cookie['value']
                    #one_cookie[cookie['name']] = cookie['value']
                    one_cookie.update([key] = value)

                requestCookiesList.append(one_cookie)


            f = open("requestCookies.txt", "w")

            for x in s.cookies:
                f.write(str(x))
            f.close()

            URL = baseURL+ "/product-category/promotions"
            page = s.get(URL, cooooookies)

            soup = BeautifulSoup(page.content, "html.parser")

            f = open("demofile3.html", "w")


            f.write(str(page.content))
            f.close()

            #results = soup.find(id="ResultsContainer")
            #results = soup.find(class_="scrollable-content")
            results = soup.find("div",{"class":"scrollable-content"})
            print(results)

            allElements = results.find_all("article", class_="_7e3920c1")

            print("tttttt")

        except Exception as ex:
            messagebox.showerror("Exception Message", "Exception: " + str(ex))
