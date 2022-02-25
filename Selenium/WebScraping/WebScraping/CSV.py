class CSV:
    def WriteCSVFile(fileName, myList):
    # open the file in the write mode
    f = open(fileName+datetime.datetime.now().strftime("_%Y%m%d_%H%M")+'.csv', 'w', encoding='UTF8')
    
    # create the csv writer
    writer = csv.writer(f)
    
    # write a row to the csv file
    writer.writerows(myList)

    for item in myList:
        writer.writerow(item)
    
    # close the file
    f.close()




