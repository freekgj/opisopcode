from database import executesql

count = 0
row_data = []
row_count = 0

def getsessions(database):
    return database.sessions.find()

def getvisitors(database):
    return database.visitors.find()

def save_order(session, sqldb):

    if "buid" in session:
        buid = str(session["buid"][0])
    else:
        return

    if "order" in session and "products" in session["order"]:
        for product_in_buid in session["order"]["products"]:
            product_ID = str(product_in_buid["id"])

            global count
            count += 1

            global row_data
            row_data.append((product_ID, buid))

            if count == 1000:
                ordersql = '''INSERT INTO orders (product_ID, buid) VALUES (\"%s\", \"%s\")'''

                global row_count
                row_count += 1
                print("orders - row " + str(row_count))
                executesql(ordersql, row_data, sqldb)
                row_data = []
                global count
                count = 0

def save_buids(visitor, sqldb):
    if "_id" in visitor:
        visitor_ID = str(visitor["_id"])
    else:
        return

    if "buids" in visitor:
        for buid in visitor["buids"]:
            browser_ID = str(buid)

            global count
            count += 1

            global row_data
            row_data.append((browser_ID, visitor_ID))

            if count == 1000:
                buidssql = '''INSERT INTO buids (buid, visitor_ID) VALUES (\"%s\", \"%s\")'''
                global row_count
                row_count += 1
                print("buids - row " + str(row_count))
                executesql(buidssql, row_data, sqldb)
                row_data = []
                global count
                count = 0