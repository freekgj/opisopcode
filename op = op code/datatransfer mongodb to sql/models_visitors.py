from database import executesql

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

def savevisitor(visitor, sqldb):
    if "_id" in visitor:
        id = str(visitor["_id"])
    else:
        return

    if "order" in visitor and "count" in visitor["order"]:
        count_of_total_bought_products = int(visitor["order"]["count"])
    else:
        count_of_total_bought_products = 0

    if "order" in visitor and "first" in visitor["order"]:
        first_order_placed = str(visitor["order"]["first"])
    else:
        first_order_placed = ""

    if "order" in visitor and "latest" in visitor["order"]:
        latest_order_placed = str(visitor["order"]["latest"])
    else:
        latest_order_placed = ""

    if "latest_activity" in visitor:
        latest_activity = str(visitor["latest_activity"])
    else:
        latest_activity = ""

    visitorsql = '''INSERT INTO visitors (
                                        visitor_ID, 
                                        count_overall_products,
                                        first_order, 
                                        latest_order, 
                                        latest_activity) 
                                        VALUES (\"%s\", \"%s\", \"%s\", \"%s\", \"%s\")'''

    row_data = [id, count_of_total_bought_products, first_order_placed, latest_order_placed, latest_activity]
    row_data_complete = []

    for item in row_data:
        checked_item = change_high_comma(item)
        row_data_complete.append(checked_item)

    executesql(visitorsql, row_data_complete, sqldb)