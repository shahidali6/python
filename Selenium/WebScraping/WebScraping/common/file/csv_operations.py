# import date and time namespace
import datetime
# import CSV namespace to read and write CSV files.
import csv

#import namespaces to show error message
from tkinter import * 
from tkinter import messagebox

# Write csv file based on the file name and list of string
class csv_operations:
    def write_csvfile(self, fileName, listToWrite):   
        try:
            # open the file in the write mode
            fileToRead = open(
                fileName + datetime.datetime.now().strftime("_%Y%m%d_%H%M")+'.csv', 'w', encoding='UTF8')

            # create the csv writer
            csvWriter = csv.writer(fileToRead)

            # write a row to the csv file
            #csvWriter.writerows(listToWrite)

            for line in listToWrite:
                csvWriter.writerow(line)

            # close the file
            fileToRead.close()
            return True
        except ex:
            messagebox.showerror("Exception Message", "Exception: "+ex)
            return False

    def read_csvfile(fileName, listToWrite):   
        try:
            # open the file in the write mode
            fileToRead = open(
                fileName + datetime.datetime.now().strftime("_%Y%m%d_%H%M")+'.csv', 'w', encoding='UTF8')

            # create the csv writer
            csvWriter = csv.writer(fileToRead)

            # write a row to the csv file
            csvWriter.writerows(listToWrite)

            for line in listToWrite:
                csvWriter.writerow(line)

            # close the file
            fileToRead.close()
        except ex:
            messagebox.showerror("Exception Message", "Exception: "+ex)