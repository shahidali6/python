from common.file.csv_operations import csv_operations
from selenium_operations.driver_chrome import driver_chrome

csv_object = csv_operations()

listss1 = ["apple", "banana"]

list_csv = csv_object.write_csvfile("myfile", listss1)

print("this si sdfs")

driver_object = driver_chrome()

baseURL = "https://www.airliftexpress.com/"
#baseURL = "https://www.google.com/"


#Fields
countryXpath = "//*[@id=\"cdk-overlay-0\"]/nz-modal-container/div/div/div/ecp-update-delivery-location/ecp-lazy-google-map-wrapper/div/div[2]/form/div/div/div[1]/nz-form-item/nz-form-control/div/div/nz-select/nz-select-top-control/nz-select-search/input"
countryText = "Pakistan"
cityxPath = "//*[@id=\"cdk-overlay-0\"]/nz-modal-container/div/div/div/ecp-update-delivery-location/ecp-lazy-google-map-wrapper/div/div[2]/form/div/div/div[2]/nz-form-item/nz-form-control/div/div/nz-select/nz-select-top-control/nz-select-search/input"
cityText = "Sialkot"
areaxPath = "//*[@id=\"cdk-overlay-0\"]/nz-modal-container/div/div/div/ecp-update-delivery-location/ecp-lazy-google-map-wrapper/div/div[2]/form/div/div[2]/div[1]/div/nz-form-item/nz-form-control/div/div/nz-select/nz-select-top-control/nz-select-search/input"
areaText = "Neka Pura, Sialkot"
nekaPuraxpath = "//*[@id=\"cdk-overlay-5\"]/nz-option-container/div/cdk-virtual-scroll-viewport/div[1]/nz-option-item[1]/div/div/strong"
continueButtonxPath = "//*[@id=\"cdk-overlay-0\"]/nz-modal-container/div/div/div/ecp-update-delivery-location/ecp-lazy-google-map-wrapper/div/div[2]/form/div/div[2]/div[3]/button"

driver_object.initiate_driver_get_cookies(baseURL, countryXpath, countryText, cityxPath, cityText, areaxPath, areaText,nekaPuraxpath, continueButtonxPath)

driver_object.initiate_driver(baseURL)
countryXpath = "//*[@id=\"cdk-overlay-0\"]/nz-modal-container/div/div/div/ecp-update-delivery-location/ecp-lazy-google-map-wrapper/div/div[2]/form/div/div/div[1]/nz-form-item/nz-form-control/div/div/nz-select/nz-select-top-control/nz-select-search/input"

driver_object.find_element_by_xpath_and_send_string_key(countryXpath, "Pakistan")

del driver_object