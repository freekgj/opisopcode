from database import executesql
import random

already_given_id = []

def get_unique_id():
    global already_given_id
    unique_id = random.randrange(100000, 999999)
    if unique_id not in already_given_id:
        already_given_id.append(unique_id)
        return unique_id
    else:
        return get_unique_id()

def getvisitors(database):
    return database.visitors.find()

def savevisitor(visitor, sqldb):
    if "_id" in visitor:
        id = visitor["_id"]
    else:
        id = int(get_unique_id())

    if "buids" in visitor:
        buids = []
        for variable in visitor["buids"]:
            buids.append(variable)
    else:
        buids = None

    if "created" in visitor["sm"]:
        account_created = visitor["sm"]["created"]
    else:
        account_created = None

    if "count" in visitor["order"]:
        overal_brought_products = visitor["order"]["count"]
    else:
        overal_brought_products = 0

    if "latest" in visitor["order"]:
        latest_order_products = visitor["order"]["latest"]
    else:
        latest_order_products = None

    if "latest_activity" in visitor:
        latest_activity = visitor["latest_activity"]
    else:
        latest_activity = "unknown"


    visitorsql = "INSERT INTO visitors (ID_visitors, buids, profile_created, overal_bought_products, latest_order_products, latest_activity) VALUES (\"{}\", \"{}\", \"{}\", {}, \"{}\", \"{}\")".format(str(id), str(buids), str(account_created), int(overal_brought_products), str(latest_order_products), str(latest_activity))
    #print(productsql)
    executesql(visitorsql, sqldb)