import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# import namespaces to show error message
# from tkinter import *
from tkinter import messagebox


class driver_chrome:
    baseURL = "https://www.airliftexpress.com/"
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
            print("tttttt")

        except Exception as ex:
            messagebox.showerror("Exception Message", "Exception: " + str(ex))
