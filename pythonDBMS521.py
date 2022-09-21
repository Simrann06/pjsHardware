##// - PJS Hardware Supply DBMS
##// - Jake Simran and Phillip
##// - 521 Final Project 

## new connection to database is established and closed with each transaction so methods can be called individually and in any order

from mysql.connector import connect, Error

#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#
##_#_#_#_#_#_#_#_#_#_#-- Methods to add product to tables
#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#


#// - Add product to cellphone and inventory tabels 
def add_product_cellphone(table, serialNumber, itemName, price):


    insert_product = "insert into cellphone (sn, itemName, price) VALUES (%s, %s, %s);"

    insert_product_vals = (
        serialNumber,
        itemName,
        price
    )
    try:
        with connect(
            host="localhost",
            user= 'root',
            password= 'T@123456',
            database="JMTechCo",
        ) as connection:
            with connection.cursor() as cursor:
                for result in cursor.execute(insert_product, insert_product_vals, multi=True):
                        if result.with_rows:
                            print(result.fetchall())
                connection.commit()
    except Error as e:
        print(e)


    insert_product_inventory = " insert into inventory (sn, itemName, price, category) VALUES (%s, %s, %s, %s);"

    insert_product_inventory_vals = (
        serialNumber,
        itemName,
        price,
        table
    )
    try:
        with connect(
            host="localhost",
            user= 'root',
            password= 'T@123456',
            database="JMTechCo",
        ) as connection:
            with connection.cursor() as cursor:
                for result in cursor.execute(insert_product_inventory, insert_product_inventory_vals, multi=True):
                        if result.with_rows:
                            print(result.fetchall())
                connection.commit()
    except Error as e:
        print(e)

    connection.close()


###############################

#// - Add product to tablet and inventory tabels 
def add_product_tablet(table, serialNumber, itemName, price):


    insert_product = "insert into tablet (sn, itemName, price) VALUES (%s, %s, %s);"

    insert_product_vals = (
        serialNumber,
        itemName,
        price
    )
    try:
        with connect(
            host="localhost",
            user= 'root',
            password= 'T@123456',
            database="JMTechCo",
        ) as connection:
            with connection.cursor() as cursor:
                for result in cursor.execute(insert_product, insert_product_vals, multi=True):
                        if result.with_rows:
                            print(result.fetchall())
                connection.commit()
    except Error as e:
        print(e)


    insert_product_inventory = " insert into inventory (sn, itemName, price, category) VALUES (%s, %s, %s, %s);"

    insert_product_inventory_vals = (
        serialNumber,
        itemName,
        price,
        table
    )
    try:
        with connect(
            host="localhost",
            user= 'root',
            password= 'T@123456',
            database="JMTechCo",
        ) as connection:
            with connection.cursor() as cursor:
                for result in cursor.execute(insert_product_inventory, insert_product_inventory_vals, multi=True):
                        if result.with_rows:
                            print(result.fetchall())
                connection.commit()
    except Error as e:
        print(e)

    connection.close()


###############################

#// - Add product to laptop and inventory tabels 
def add_product_laptop(table, serialNumber, itemName, price):


    insert_product = "insert into laptop (sn, itemName, price) VALUES (%s, %s, %s);"

    insert_product_vals = (
        serialNumber,
        itemName,
        price
    )
    try:
        with connect(
            host="localhost",
            user= 'root',
            password= 'T@123456',
            database="JMTechCo",
        ) as connection:
            with connection.cursor() as cursor:
                for result in cursor.execute(insert_product, insert_product_vals, multi=True):
                        if result.with_rows:
                            print(result.fetchall())
                connection.commit()
    except Error as e:
        print(e)


    insert_product_inventory = " insert into inventory (sn, itemName, price, category) VALUES (%s, %s, %s, %s);"

    insert_product_inventory_vals = (
        serialNumber,
        itemName,
        price,
        table
    )
    try:
        with connect(
            host="localhost",
            user= 'root',
            password= 'T@123456',
            database="JMTechCo",
        ) as connection:
            with connection.cursor() as cursor:
                for result in cursor.execute(insert_product_inventory, insert_product_inventory_vals, multi=True):
                        if result.with_rows:
                            print(result.fetchall())
                connection.commit()
    except Error as e:
        print(e)

    connection.close()


#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#
##_#_#_#_#_#_#_#_#_#_#-- Methods to remove products from tables
#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#

#// - remove products from cellphone and inventory tabels 
def remove_product_cellphone(serialNumber):

    delete_product = "DELETE FROM cellphone WHERE sn = '%s'"

    delete_vals = (
    serialNumber,
    )

    try:
        with connect(
            host="localhost",
            user= 'root',
            password= 'T@123456',
            database="JMTechCo",
        ) as connection:
            with connection.cursor() as cursor:
                for result in cursor.execute(delete_product, delete_vals, multi=True):
                        if result.with_rows:
                            print(result.fetchall())
                connection.commit()
    except Error as e:
        print(e)


    delete_product_inventory = "DELETE FROM inventory WHERE sn = '%s'"

    delete_vals_inventory = (
    serialNumber,
    )

    try:
        with connect(
            host="localhost",
            user= 'root',
            password= 'T@123456',
            database="JMTechCo",
        ) as connection:
            with connection.cursor() as cursor:
                for result in cursor.execute(delete_product_inventory, delete_vals_inventory, multi=True):
                        if result.with_rows:
                            print(result.fetchall())
                connection.commit()
    except Error as e:
        print(e)

    connection.close()

###############################

#// - remove products from tablet and inventory tabels 
def remove_product_tablet(serialNumber):

    delete_product = "DELETE FROM tablet WHERE sn = '%s'"

    delete_vals = (
    serialNumber,
    )

    try:
        with connect(
            host="localhost",
            user= 'root',
            password= 'T@123456',
            database="JMTechCo",
        ) as connection:
            with connection.cursor() as cursor:
                for result in cursor.execute(delete_product, delete_vals, multi=True):
                        if result.with_rows:
                            print(result.fetchall())
                connection.commit()
    except Error as e:
        print(e)


    delete_product_inventory = "DELETE FROM inventory WHERE sn = '%s'"

    delete_vals_inventory = (
    serialNumber,
    )

    try:
        with connect(
            host="localhost",
            user= 'root',
            password= 'T@123456',
            database="JMTechCo",
        ) as connection:
            with connection.cursor() as cursor:
                for result in cursor.execute(delete_product_inventory, delete_vals_inventory, multi=True):
                        if result.with_rows:
                            print(result.fetchall())
                connection.commit()
    except Error as e:
        print(e)

    connection.close()

###############################

#// - remove products from laptop and inventory tabels 
def remove_product_laptop(serialNumber):

    delete_product = "DELETE FROM tablet WHERE sn = '%s'"

    delete_vals = (
    serialNumber,
    )

    try:
        with connect(
            host="localhost",
            user= 'root',
            password= 'T@123456',
            database="JMTechCo",
        ) as connection:
            with connection.cursor() as cursor:
                for result in cursor.execute(delete_product, delete_vals, multi=True):
                        if result.with_rows:
                            print(result.fetchall())
                connection.commit()
    except Error as e:
        print(e)


    delete_product_inventory = "DELETE FROM inventory WHERE sn = '%s'"

    delete_vals_inventory = (
    serialNumber,
    )

    try:
        with connect(
            host="localhost",
            user= 'root',
            password= 'T@123456',
            database="JMTechCo",
        ) as connection:
            with connection.cursor() as cursor:
                for result in cursor.execute(delete_product_inventory, delete_vals_inventory, multi=True):
                        if result.with_rows:
                            print(result.fetchall())
                connection.commit()
    except Error as e:
        print(e)

    connection.close()

#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#
##_#_#_#_#_#_#_#_#_#_#-- Methods to edit existing products in tables 
#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#

#// - edit existing products in cellphone and inventory tabels 
def edit_product_cellphone(serialNumber, variable, value):

    update_product = "UPDATE cellphone SET %s = '%s' WHERE sn = '%s'"

    update_vals_ = (
    variable,
    value,
    serialNumber
    )

    try:
        with connect(
            host="localhost",
            user= 'root',
            password= 'T@123456',
            database="JMTechCo",
        ) as connection:
            with connection.cursor() as cursor:
                for result in cursor.execute(update_product, update_vals_, multi=True):
                        if result.with_rows:
                            print(result.fetchall())
                connection.commit()
    except Error as e:
        print(e)


    
    update_product_inventory = "UPDATE inventory SET %s = '%s' WHERE sn = '%s'"

    update_vals_inventory = (
    variable,
    value,
    serialNumber
    )

    try:
        with connect(
            host="localhost",
            user= 'root',
            password= 'T@123456',
            database="JMTechCo",
        ) as connection:
            with connection.cursor() as cursor:
                for result in cursor.execute(update_product_inventory, update_vals_inventory, multi=True):
                        if result.with_rows:
                            print(result.fetchall())
                connection.commit()
    except Error as e:
        print(e)

###############################

#// - edit existing products in tablet and inventory tabels 
def edit_product_tablet(serialNumber, variable, value):

    update_product = "UPDATE tablet SET %s = '%s' WHERE sn = '%s'"

    update_vals_ = (
    variable,
    value,
    serialNumber
    )

    try:
        with connect(
            host="localhost",
            user= 'root',
            password= 'T@123456',
            database="JMTechCo",
        ) as connection:
            with connection.cursor() as cursor:
                for result in cursor.execute(update_product, update_vals_, multi=True):
                        if result.with_rows:
                            print(result.fetchall())
                connection.commit()
    except Error as e:
        print(e)


    
    update_product_inventory = "UPDATE inventory SET %s = '%s' WHERE sn = '%s'"

    update_vals_inventory = (
    variable,
    value,
    serialNumber
    )

    try:
        with connect(
            host="localhost",
            user= 'root',
            password= 'T@123456',
            database="JMTechCo",
        ) as connection:
            with connection.cursor() as cursor:
                for result in cursor.execute(update_product_inventory, update_vals_inventory, multi=True):
                        if result.with_rows:
                            print(result.fetchall())
                connection.commit()
    except Error as e:
        print(e)

###############################

#// - edit existing products in laptop and inventory tabels 
def edit_product_laptop(serialNumber, variable, value):

    update_product = "UPDATE laptop SET %s = '%s' WHERE sn = '%s'"

    update_vals_ = (
    variable,
    value,
    serialNumber
    )

    try:
        with connect(
            host="localhost",
            user= 'root',
            password= 'T@123456',
            database="JMTechCo",
        ) as connection:
            with connection.cursor() as cursor:
                for result in cursor.execute(update_product, update_vals_, multi=True):
                        if result.with_rows:
                            print(result.fetchall())
                connection.commit()
    except Error as e:
        print(e)


    
    update_product_inventory = "UPDATE inventory SET %s = '%s' WHERE sn = '%s'"

    update_vals_inventory = (
    variable,
    value,
    serialNumber
    )

    try:
        with connect(
            host="localhost",
            user= 'root',
            password= 'T@123456',
            database="JMTechCo",
        ) as connection:
            with connection.cursor() as cursor:
                for result in cursor.execute(update_product_inventory, update_vals_inventory, multi=True):
                        if result.with_rows:
                            print(result.fetchall())
                connection.commit()
    except Error as e:
        print(e)

#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#
##_#_#_#_#_#_#_#_#_#_#-- Main Method
#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#

def main():

    table = "cellphone"
    serialNumber = 321654987
    itemName = "iphon 69"
    price = 6969

    add_product_cellphone(table, serialNumber, itemName, price)

    #table = "laptop"
    #serialNumber = 56789
    #itemName = "laptop 69"
    #price = 420
#
    #add_product_laptop(table, serialNumber, itemName, price)
#
    #table = "tablet"
    #serialNumber = 78945613
    #itemName = "tablet 69"
    #price = 69
#
    #add_product_tablet(table, serialNumber, itemName, price)

# need to test all functions 

# add transaction checks? 

# add extra queries to verify entries?

## web app will evaluate first digit of serial number entered to determine which table it needs to access (3 for phone, 5 for laptop) 
##          then will call the method needed for the operation passing the parameters entered into the web app to said method)

    if __name__ == "__main__":
        main()