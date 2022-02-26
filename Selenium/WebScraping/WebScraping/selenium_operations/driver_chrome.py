from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#import namespaces to show error message
from tkinter import * 
from tkinter import messagebox

class driver_chrome:
    baseURL = "https://www.airliftexpress.com/"
    def initiate_driver(self, base_url):
        try:
            driver = webdriver.Chrome()
            baseURL = base_url
            driver.get(base_url)
        except ex:
            messagebox.showerror("Exception Message", "Exception: "+ex)