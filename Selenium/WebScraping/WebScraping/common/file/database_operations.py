import mysql.connector
import datetime

class database_operations():
    def InsertDataIntoMySQL(list_to_insert_database):
        # Insert Data into MySQL
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="python"
            # mydb = mysql.connector.connect(
            #  host="db-python-webscraping.cpxtybckovvs.us-east-2.rds.amazonaws.com",
            #  user="dbadmin",
            #  password="Aesn8POSA2kTzjt1GAk9",
            #  database="db-python-webscraping"
        )

        mycursor = mydb.cursor()

        for item in list_to_insert_database:
            sql = "INSERT INTO olx (title, pricestart,priceend, location,image,link,feature) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (item)
            mycursor.execute(sql, val)
            mydb.commit()

        print(mycursor.rowcount, "record inserted in MytSQL Database.")

    def insert_data_into_airlift_table(self, list_to_insert_database):
        # Insert Data into MySQL
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="python"
        )
        mycursor = mydb.cursor()

        sql = "INSERT INTO airlift (name,price,image,link,coin,orignal_price,discount_percentage,product_avalible,location) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        mycursor.execute(sql, list_to_insert_database)
        mydb.commit()

        print(mycursor.rowcount, "record inserted in MytSQL Database.")
