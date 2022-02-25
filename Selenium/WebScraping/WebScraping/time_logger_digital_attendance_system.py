from common.file.csv_operations import csv_operations

csv_object = csv_operations()

listss1 = ["apple", "banana"]

list_csv = csv_object.write_csvfile("myfile", listss1)
list_csv_read = csv_object.read_csvfile(r"C:\Users\shahid\source\repos\shahidali6\python\Selenium\WebScraping\WebScraping\olx.csv")

print("this si sdfs")

