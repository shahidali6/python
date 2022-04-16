import mysql.connector
import datetime
#for delay
import time

class database_operations():
    def InsertDataIntoMySQL(list_to_insert_database):
        # Insert Data into MySQL
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="python")

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

    def insert_data_into_mysql_table(self, list_to_insert, host, database, user, passw, query):
        #Feilds
        product_id = image_id = link_id = product_available_id = location_id = source_id = 0
        querrrr = ''
        # Insert Data into MySQL
        mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=passw,
            database=database
        )
        mycursor = mydb.cursor()
        mycursor.execute("SHOW columns FROM airlift")
        for column in mycursor.fetchall():
            if column[0] == 'name':
                querrrr = f'INSERT IGNORE INTO airlift_product (product_name) VALUES (\'{list_to_insert[0]}\')'
                mycursor.execute(querrrr)
                mydb.commit()
                querrrr=''
                # Last row was ignored                
                if mycursor.lastrowid == 0:
                    mycursor.execute(f'SELECT product_id FROM airlift_product WHERE product_name = \'{list_to_insert[0]}\';')
                    rows = mycursor.fetchall()
                    product_id = rows[0][0]
                else:
                    product_id = mycursor.lastrowid
                
            if column[0] == 'image':
                querrrr = f'INSERT IGNORE INTO airlift_image (image_link) VALUES (\'{list_to_insert[3]}\')'
                mycursor.execute(querrrr)
                mydb.commit()
                querrrr=''
                # Last row was ignored                
                if mycursor.lastrowid == 0:
                    mycursor.execute(f'SELECT image_id FROM airlift_image WHERE image_link = \'{list_to_insert[3]}\';')
                    rows = mycursor.fetchall()
                    image_id = rows[0][0]
                else:
                    image_id = mycursor.lastrowid

            if column[0] == 'category':
                querrrr = f'INSERT IGNORE INTO airlift_category (category_name) VALUES (\'{list_to_insert[1]}\')'
                mycursor.execute(querrrr)
                mydb.commit()
                querrrr=''
                # Last row was ignored                
                if mycursor.lastrowid == 0:
                    mycursor.execute(f'SELECT category_id FROM airlift_category WHERE category_name = \'{list_to_insert[1]}\';')
                    rows = mycursor.fetchall()
                    category_id = rows[0][0]
                else:
                    category_id = mycursor.lastrowid

            if column[0] == 'link':
                querrrr = f'INSERT IGNORE INTO airlift_links (link_value) VALUES (\'{list_to_insert[4]}\')'
                mycursor.execute(querrrr)
                mydb.commit()
                querrrr=''
                # Last row was ignored                
                if mycursor.lastrowid == 0:
                    mycursor.execute(f'SELECT link_id FROM airlift_links WHERE link_value = \'{list_to_insert[4]}\';')
                    rows = mycursor.fetchall()
                    link_id = rows[0][0]
                else:
                    link_id = mycursor.lastrowid
                
            if column[0] == 'location':
                querrrr = f'INSERT IGNORE INTO airlift_location (location_name) VALUES (\'{list_to_insert[9]}\')'
                mycursor.execute(querrrr)
                mydb.commit()
                querrrr=''
                # Last row was ignored                
                if mycursor.lastrowid == 0:
                    mycursor.execute(f'SELECT location_id FROM airlift_location WHERE location_name = \'{list_to_insert[9]}\';')
                    rows = mycursor.fetchall()
                    location_id = rows[0][0]
                else:
                    location_id = mycursor.lastrowid

            if column[0] == 'product_avalible':
                querrrr = f'INSERT IGNORE INTO airlift_stock (stock_value) VALUES (\'{list_to_insert[8]}\')'
                mycursor.execute(querrrr)
                mydb.commit()
                querrrr=''
                # Last row was ignored                
                if mycursor.lastrowid == 0:
                    mycursor.execute(f'SELECT stock_id FROM airlift_stock WHERE  stock_value = \'{list_to_insert[8]}\';')
                    rows = mycursor.fetchall()
                    stock_id = rows[0][0]
                else:
                    stock_id = mycursor.lastrowid

            if column[0] == 'source':
                querrrr = f'INSERT IGNORE INTO source (source_name) VALUES (\'{list_to_insert[10]}\')'
                mycursor.execute(querrrr)
                mydb.commit()
                querrrr=''
                # Last row was ignored                
                if mycursor.lastrowid == 0:
                    mycursor.execute(f'SELECT source_id FROM source WHERE  source_name = \'{list_to_insert[10]}\';')
                    rows = mycursor.fetchall()
                    source_id = rows[0][0]
                else:
                    source_id = mycursor.lastrowid

        list_to_insert[0] = product_id
        list_to_insert[1] = category_id
        list_to_insert[3] = image_id
        list_to_insert[4] = link_id
        list_to_insert[8] = stock_id
        list_to_insert[9] = location_id
        list_to_insert[10] = source_id

        #print[column[0] for column in cursor.fetchall()]

        sql = query
        mycursor.execute(sql, list_to_insert)
        mydb.commit()
        mydb.close()