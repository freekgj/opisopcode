from database import executesql

def getsessions(database):
    return database.sessions.find()

def getvisitors(database):
    return database.visitors.find()

def change_high_comma(item):
    if type(item) == str:
        if "'" in item or '"' in item:
            item = item.replace("'", "")
            item = item.replace('"', "")
            return item
        return item
    return item

def save_order(session, sqldb):
    if ("buid" in session) and session["buid"] != None:
        buid = str(session["buid"][0])
    else:
        return

    if "order" in session and "products" in session["order"]:
        for product_in_buid in session["order"]["products"]:
            product_ID = str(product_in_buid["id"])

            ordersql = '''INSERT INTO orders (product_ID, buid) VALUES (%s, %s)'''

            row_data = [product_ID, buid]
            row_data_complete = []

            for item in row_data:
                checked_item = change_high_comma(item)
                row_data_complete.append(checked_item)

            executesql(ordersql, row_data_complete, sqldb)

def save_buids(visitor, sqldb):
    if "_id" in visitor:
        visitor_ID = str(visitor["_id"])
    else:
        return

    if "buids" in visitor:
        for buid in visitor["buids"]:
            browser_ID = str(buid)

            buidssql = '''INSERT INTO buids (buid, visitor_ID) VALUES (%s, %s)'''

            row_data = [browser_ID, visitor_ID]
            row_data_complete = []

            for item in row_data:
                checked_item = change_high_comma(item)
                row_data_complete.append(checked_item)

            executesql(buidssql, row_data_complete, sqldb)