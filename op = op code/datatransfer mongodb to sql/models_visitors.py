from database import executesql

count = 0
row_data = []
row_count = 0

def getvisitors(database):
    return database.visitors.find()

def savevisitor(visitor, sqldb):
    if "_id" in visitor:
        id = str(visitor["_id"])
    else:
        return

    if "count" in visitor["order"]:
        count_of_total_bought_products = int(visitor["order"]["count"])
    else:
        count_of_total_bought_products = None

    if "first" in visitor["order"]:
        first_order_placed = str(visitor["order"]["first"])
    else:
        first_order_placed = ""

    if "latest" in visitor["order"]:
        latest_order_placed = str(visitor["order"]["latest"])
    else:
        latest_order_placed = ""

    if "latest_activity" in visitor:
        latest_activity = str(visitor["latest_activity"])
    else:
        latest_activity = ""

    global count
    count += 1

    global row_data
    row_data.append((id, count_of_total_bought_products, first_order_placed, latest_order_placed, latest_activity))

    if count == 1000:
        visitorsql = '''INSERT INTO visitors (
                                    visitor_ID, 
                                    count_overall_bought_products,
                                    first_order, 
                                    latest_order, 
                                    latest_activity) VALUES (\"{}\", {}, \"{}\", \"{}\", \"{}\")'''
        global row_count
        row_count += 1
        print("visitors - row " + str(row_count))
        executesql(visitorsql, row_data, sqldb)
        row_data = []
        global count
        count = 0