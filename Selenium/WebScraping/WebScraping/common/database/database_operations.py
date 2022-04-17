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
        product_id_value = image_id_value = link_id_value = product_available_id_value = location_id_value = source_id_value_value = 0
        #Column names
        name = 'name'
        image = 'image'
        category = 'category'
        link  ='link'
        location = 'location'
        product_avalible = 'product_avalible'
        source = 'source'

        #Table names their column names
        airlift = 'airlift'
        airlift_product = 'airlift_product'
        product_name = 'product_name'
        product_id = 'product_id'
        airlift_image = 'airlift_image'
        image_id = 'image_id'
        image_link = 'image_link'
        airlift_category = 'airlift_category'
        category_id = 'category_id'
        category_name = 'category_name'
        airlift_links = 'airlift_links'
        link_value = 'link_value'
        airlift_location = 'airlift_location'
        location_name = 'location_name'
        airlift_stock = 'airlift_stock'
        stock_value = 'stock_value'
        source_name = 'source_name'

        query = ''
        # Insert Data into MySQL
        mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=passw,
            database=database
        )
        mycursor = mydb.cursor()
        mycursor.execute(f'SHOW columns FROM {airlift}')
        for column in mycursor.fetchall():
            if column[0] == name:
                query = f'INSERT IGNORE INTO {airlift_product} ({product_name}) VALUES (\'{list_to_insert[0]}\')'
                mycursor.execute(query)
                mydb.commit()
                query=''
                # Last row was ignored                
                if mycursor.lastrowid == 0:
                    mycursor.execute(f'SELECT {product_id} FROM {airlift_product} WHERE {product_name} = \'{list_to_insert[0]}\';')
                    rows = mycursor.fetchall()
                    product_id_value = rows[0][0]
                else:
                    product_id_value = mycursor.lastrowid
                
            if column[0] == image:
                query = f'INSERT IGNORE INTO {airlift_image} ({image_link}) VALUES (\'{list_to_insert[3]}\')'
                mycursor.execute(query)
                mydb.commit()
                query=''
                # Last row was ignored                
                if mycursor.lastrowid == 0:
                    mycursor.execute(f'SELECT {image_id} FROM {airlift_image} WHERE {image_link} = \'{list_to_insert[3]}\';')
                    rows = mycursor.fetchall()
                    image_id_value = rows[0][0]
                else:
                    image_id_value = mycursor.lastrowid

            if column[0] == category:
                query = f'INSERT IGNORE INTO {airlift_category} ({category_name}) VALUES (\'{list_to_insert[1]}\')'
                mycursor.execute(query)
                mydb.commit()
                query=''
                # Last row was ignored                
                if mycursor.lastrowid == 0:
                    mycursor.execute(f'SELECT {category_id} FROM {airlift_category} WHERE {category_name} = \'{list_to_insert[1]}\';')
                    rows = mycursor.fetchall()
                    category_id_value = rows[0][0]
                else:
                    category_id_value = mycursor.lastrowid

            if column[0] == link:
                query = f'INSERT IGNORE INTO {airlift_links} ({link_value}) VALUES (\'{list_to_insert[4]}\')'
                mycursor.execute(query)
                mydb.commit()
                query=''
                # Last row was ignored                
                if mycursor.lastrowid == 0:
                    mycursor.execute(f'SELECT {link_id} FROM {airlift_links} WHERE {link_value} = \'{list_to_insert[4]}\';')
                    rows = mycursor.fetchall()
                    link_id_value = rows[0][0]
                else:
                    link_id_value = mycursor.lastrowid
                
            if column[0] == location:
                query = f'INSERT IGNORE INTO {airlift_location} ({location_name}) VALUES (\'{list_to_insert[9]}\')'
                mycursor.execute(query)
                mydb.commit()
                query=''
                # Last row was ignored                
                if mycursor.lastrowid == 0:
                    mycursor.execute(f'SELECT {location_id} FROM {airlift_location} WHERE {location_name} = \'{list_to_insert[9]}\';')
                    rows = mycursor.fetchall()
                    location_id_value = rows[0][0]
                else:
                    location_id_value = mycursor.lastrowid

            if column[0] == product_avalible:
                query = f'INSERT IGNORE INTO {airlift_stock} ({stock_value}) VALUES (\'{list_to_insert[8]}\')'
                mycursor.execute(query)
                mydb.commit()
                query=''
                # Last row was ignored                
                if mycursor.lastrowid == 0:
                    mycursor.execute(f'SELECT {stock_id} FROM {airlift_stock} WHERE  {stock_value} = \'{list_to_insert[8]}\';')
                    rows = mycursor.fetchall()
                    stock_id_value = rows[0][0]
                else:
                    stock_id_value = mycursor.lastrowid

            if column[0] == source:
                query = f'INSERT IGNORE INTO {source} ({source_name}) VALUES (\'{list_to_insert[10]}\')'
                mycursor.execute(query)
                mydb.commit()
                query=''
                # Last row was ignored                
                if mycursor.lastrowid == 0:
                    mycursor.execute(f'SELECT {source_id} FROM {source} WHERE {source_name} = \'{list_to_insert[10]}\';')
                    rows = mycursor.fetchall()
                    source_id_value = rows[0][0]
                else:
                    source_id_value = mycursor.lastrowid

        list_to_insert[0] = product_id_value
        list_to_insert[1] = category_id_value
        list_to_insert[3] = image_id_value
        list_to_insert[4] = link_id_value
        list_to_insert[8] = stock_id_value
        list_to_insert[9] = location_id_value
        list_to_insert[10] = source_id_value

        sql = query
        mycursor.execute(sql, list_to_insert)
        mydb.commit()
        mydb.close()