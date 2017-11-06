import sqlite3
import random
import datetime

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
    userType = 0

    while( userType != 4):
        print("1 : Agent login"
            "2 : Customer login"
            "3 : Customer signup"
            "4 : Quit")
        try:
            userType = input("Please type in the corresponding number")
            userType += 1
            userType -= 1
            if (userType <= 0 or userType >= 5):
                raise Exception("Please enter a number from 1-4")
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

        except TypeError:
            raise TypeError("Incorrect data format, please enter an integer")




def agentsF():
    global connection, cursor
    agentInput = 0
    orderInput = 0

    while (agentInput != 4):
        print("1 : Set up a delivery"
              "2 : Update a delivery"
              "3 : Add to stock"
              "4 : Logout")
        try:
            agentInput = input("Please type in the corresponding number")
            agentInput += 1
            agentInput -= 1
            if (agentInput <= 0 or agentInput >= 5):
                raise Exception("Please enter a number from 1-4")

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
                        while True:
                            pickUp = raw_input("Please enter the pickup date or leave it blank")
                            try:
                                if (pickUp == ()):
                                    print("No pick up time entered\n")
                                    break
                                if (datetime.datetime.strptime(pickUp, '%Y-%m-%d'))
                                    print("Pick up time updated\n")
                                    break

                            except ValueError:
                                raise ValueError("Incorrect data format, should be YYYY-MM-DD")

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
                    print(rows)
                    editOrder = raw_input("Would you like to edit an order? (yes/no)")
                    if (editOrder == yes):
                        orderNumber = input("Please enter the order number")
                        cursor.execute()  # placeholder
                        row = cursor.fetchone(0)
                        if (row == orderNumber):

                            while (orderInput != 4):
                                print("1 : Update pickup time"
                                      "2 : Update drop off time"
                                      "3 : Remove order"
                                      "4 : Back")
                                cursor.execute()  # placeholder
                                row = cursor.fetchone(0)
                                print (row)
                                try:
                                    orderInput = input("Please type in the corresponding number")
                                    orderInput += 1
                                    orderInput -= 1
                                    if (orderInput <= 0 or orderInput >= 5):
                                        raise Exception("Please enter a number from 1-4")

                                    if (orderInput == 1):
                                        while True:
                                            newTime = raw_input("Please enter a new pickup time")
                                            try:
                                                datetime.datetime.strptime(newTime, '%Y-%m-%d')
                                                cursor.execute()  # placeholder
                                                print("Pick up time updated")
                                                break

                                            except ValueError:
                                                raise ValueError("Incorrect data format, should be YYYY-MM-DD")

                                    if (orderInput == 2):
                                        while True:
                                            newTime = raw_input("Please enter a new drop off time")
                                            try:
                                                datetime.datetime.strptime(newTime, '%Y-%m-%d')
                                                cursor.execute()  # placeholder
                                                print("Drop off time updated")
                                                break

                                            except ValueError:
                                                raise ValueError("Incorrect data format, should be YYYY-MM-DD")

                                    if (orderInput == 3):
                                        cursor.execute()  # placeholder
                                        print("Order removed\n")

                                    if (agentInput == 4):
                                        quit()

                                except TypeError:
                                    raise TypeError("Incorrect data format, please enter an integer")

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

        except TypeError:
            raise TypeError("Incorrect data format, please enter an integer")


def customersF(cid):
    global connection, cursor
    basket = []
    unavailable = []
    customerInput = 0

    while (customerInput != 4):
        print("1 : Search for products"
              "2 : Place an order"
              "3 : List orders"
              "4 : Logout")
        try:
            customerInput = input("Please type in the corresponding number")
            customerInput += 1
            customerInput -= 1
            if (customerInput <= 0 or customerInput >= 5):
                raise Exception("Please enter a number from 1-4")
            if (customerInput == 1):
                print("Search for products\n")
                print("Please enter product keywords\n")

            if (customerInput == 2):
                print("Place an order\n")
                if not basket:
                    print("Basket is empty")
                    continue
                cursor.execute() #placeholder search to verify that all items in the basket are available
                rows = cursor.fetchall()
                for i in rows:
                    unavailable.append(i)
                if not unavailable:
                    cursor.execute() #placeholder place whole basket into database
                    print("All items in basket are ordered")
                    continue

                for i in unavailable[i][0]:
                    row = cursor.fetchrow(i)
                    print("Product " + row + " is unavailable\n")
                    print("1 : change quantity"
                          "2 : Remove product from basket")
                    changeProduct = input("Please type in the corresponding number")
                    if (changeProduct == 1):
                        while True:
                            try:
                                newQuantity = input("Please enter a new quantity: ")
                                newQuantity += 1
                                newQuantity -= 1
                                cursor.execute()#placeholder to ensure it's a viable number
                                row = cursor.fetchone(0)
                                if (row == ()):
                                    raise Exception("Not a viable quantity")

                                if product in basket: basket.remove(product)
                                product = (sid, pid, newQuantity)
                                basket.append(product)
                                break

                            except TypeError:
                                raise TypeError("Incorrect data format, please enter an integer")

                    if (changeProduct == 2):
                        while product in basket: basket.remove(product)


                cursor.execute() #place holder put items from the basket into database as orders'
                print("All items in basket are ordered")

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
                    if (seeMore != "yes"):
                        break

            if (customerInput == 4):
                quit()

        except TypeError:
            raise TypeError("Incorrect data format, please enter an integer")

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