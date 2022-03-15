# import date and time namespace
import datetime
# import CSV namespace to read and write CSV files.
import csv
from os import read

# import namespaces to show error message
#from tkinter import *
from tkinter import messagebox

# Write csv file based on the file name and list of string

class csv_operations:
    def write_csvfile(self, fileName, listToWrite):
        try:
            # open the file in the write mode
            fileToRead = open(
                fileName + datetime.datetime.now().strftime("_%Y%m%d_%H%M")+'.csv', 'w', newline='', encoding='UTF8')

            # create the csv writer
            csvWriter = csv.writer(fileToRead)

            # write a row to the csv file
            csvWriter.writerows(listToWrite)

            # for line in listToWrite:
            #    csvWriter.writerow(line)

            # close the file
            fileToRead.close()
            return True
        except Exception as ex:
            messagebox.showerror("Exception Message", "Exception: "+str(ex))
            return False

    def read_csvfile(self, fileName):
        try:
            return_list = []
            with open(fileName, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
                    if len(row) > 0:
                        return_list.append(row)
            return return_list
        except Exception as ex:
            messagebox.showerror("Exception Message", "Exception: "+str(ex))

    def remove_first_line_of_file(self, fileName):
        try:
            with open(fileName, 'r') as fin:
                data = fin.read().splitlines(True)
            with open(fileName, 'w') as fout:
                fout.writelines(data[1:])
            return True
        except Exception as ex:
            messagebox.showerror("Exception Message", "Exception: "+str(ex))
            return False

    def save_webpage_source(self, file_name, page_source):
        try:
            with open(file_name, 'w') as f:
                f.write(page_source)
            return True
        except Exception as ex:
            messagebox.showerror("Exception Message", "Exception: "+str(ex))
            return False

    def write_list_to_csv(self, fileName, listToWrite):
        # field names
        fields = ['Name', 'Branch', 'Year', 'CGPA']
        fileName = fileName + datetime.datetime.now().strftime("_%Y%m%d_%H%M")+'.csv'
        # data rows of csv file
        # rows = [ ['Nikhil', 'COE', '2', '9.0'],
        #  ['Sanchit', 'COE', '2', '9.1'],
        #  ['Aditya', 'IT', '2', '9.3'],
        #  ['Sagar', 'SE', '1', '9.5'],
        #  ['Prateek', 'MCE', '3', '7.8'],
        #  ['Sahil', 'EP', '2', '9.1']]

        with open(fileName, 'w', newline='') as f:

            # using csv.writer method from CSV package
            write = csv.writer(f)

            write.writerow(fields)
            write.writerows(listToWrite)

    def write_list_to_txt(self, fileName, listToWrite):
        # field names
        fields = ['Name', 'Branch', 'Year', 'CGPA']
        fileName = fileName + datetime.datetime.now().strftime("_%Y%m%d_%H%M")+'.txt'

        with open(fileName, 'w', newline='') as f:

            # using csv.writer method from CSV package
            write = csv.writer(f)

            write.writerow(fields)
            for line in listToWrite:
                array = line.split(',')
                write.writerow(array)
