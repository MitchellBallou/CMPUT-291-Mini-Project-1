import sqlite3
import random

connection = None
cursor = None

def connect(path):
    global connection, cursor

    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(' PRAGMA forteign_keys=ON; ')
    connection.commit()
    return



def login():
    global connection, cursor

    while( userType != 4):
        print("1 : Agent login"
            "2 : Customer login"
            "3 : Customer signup"
            "4 : Quit")
        userType = input("Please type in the corresponding number")

        if (userType == 1):
            print("Agent Login\n")
            aid = raw_input("Please enter your aid:")
            pwd = raw_input("Please enter your pwd:")
            cursor.execute("SELECT A.aid FROM agent A WHERE aid=:A.aid AND pwd=:A.pwd")
            row = cursor.fetchone(0)
            if (row == aid):
                print(aid + " logged in\n")
                return userType, aid
            else:
                print("invalid login")

        if (userType == 2):
            print("Customer Login\n")
            cid = raw_input("Please enter your cid:")
            pwd = raw_input("Please enter your pwd:")
            cursor.execute("SELECT C.cid FROM customers C WHERE cid=:C.cid AND pwd=:C.pwd")
            row = cursor.fetchone(0)
            if (row == cid):
                print(cid + " logged in\n")
                return userType, cid
            else:
                print("invalid login")

        if (userType == 3):
            print("Customer Signup\n")
            cid = raw_input("Please enter a cid:")
            pwd = raw_input("Please enter a pwd:")
            cursor.execute("SELECT C.cid FROM customers C WHERE cid=:C.cid")
            row = cursor.fetchone(0)
            if (row == cid):
                print(cid + " is not a unique cid")
            else:
                print("That's a unique cid\n")
                name = raw_input("Please enter your name")
                address = raw_input("Please enter your address")
                newCustomer = '''
                                    ("INSERT INTO customers(cid. name, address, pwd) VALUES
                                        (cid=:cid, name=:name, address=:address, pwd=:pwd);
                            '''
                cursor.execute(newCustomer)
                connection.commit()
                print("Signup successful\n")
                userType = 2
                return userType, cid

        if (userType == 4):
            quit()

def agentsF():
    global connection, cursor

    while (agentInput != 4):
        print("1 : Set up a delivery"
              "2 : Update a delivery"
              "3 : Add to stock"
              "4 : Logout")
        agentInput = input("Please type in the corresponding number")

        if (agentInput == 1):
            print("Set up a delivery\n")
            while True:
                trackingNumber = random.randint(100, 100000)
                cursor.execute("SELECT D.trackingNo FROM deliveries D WHERE trackingNumber=:D.trackingNo")
                row = cursor.fetchone(0)
                if (row == ()):
                    break

            print("New delivery created, tracking number: " + trackingNumber)
            while True:
                addOrder = raw_input("Would you like to add a delivery to this order? (yes/no): ")
                if (addOrder == "yes"):
                    oid = input("Please enter an oid that you want to add to this delivery")
                    pickUp = raw_input("Please enter the pickup date or leave it blank")
                    newDelivery = () #placeholder
                    cursor.execute(newDelivery)
                if (addOrder == "no"):
                    break


        if (agentInput == 2):
            print("Update a delivery\n")
            trackingNumber = input("Please enter a tracking number: ")
            cursor.execute()  # placeholder
            row = cursor.fetchone(0)

            if (row == trackingNumber):
                cursor.execute() #placeholder
                rows = cursor.fetchall()
                print rows

            else:
                print("not a valid input\n")



        if (agentInput == 3):
            print("Add to stock\n")
            sid = raw_input("Please enter your sid:")
            pid = raw_input("Please enter your pid:")
            cursor.execute()#placeholder
            row = cursor.fetchone(0)
            if (row[0] == sid and row[1] == pid):
                qty = input("How many products would you like to add to the store?")
                cursor.execute()#placeholder
                print("Quantity Updated")
                updatePrice = raw_input("Would you like to update the price of the product in this store? (yes/no)")
                if (updatePrice == "yes"):
                    cursor.execute()
                    print("Price updated\n")
            else:
                print("not a valid input\n")

        if (agentInput == 4):
            quit()

def customersF(cid):
    global connection, cursor

    while (customerInput != 4):
        print("1 : Search for products"
              "2 : Place an order"
              "3 : List orders"
              "4 : Logout")
        customerInput = input("Please type in the corresponding number")

        if (customerInput == 3):
            print("List orders\n")
            cursor.execute()#placeholder
            listSize = 5
            while True:
                rows = cursor.fetchmany(listSize)
                if (rows == ()):
                    print("No more orders.\n")
                    break
                print(rows)
                seeMore = raw_input("Would you like to see more? (yes/no)")
                if (seeMore != yes):
                    break


        if (customerInput == 4):
            quit()

def main():
    global connection, cursor

    path = "./miniProject1.db"
    connect(path)
    userType, id = login()

    if (userType == 1):
        agentsF()
    if (userType == 2):
        customersF(id)


    connection.commit()
    connection.close()
    return


if __name__ == "__main__":
    main()