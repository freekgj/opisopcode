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

def getproducts(database):
    return database.sessions.find()

def saveproduct(sessions, sqldb):
    if "_id" in sessions:
        id = sessions["_id"]
    else:
        id = int(get_unique_id())

    if "start_session" in sessions:
        start_session = sessions["session_start"]
    else:
        start_session = "no_start_session"

    if "end_session" in sessions:
        end_session = sessions["end_session"]
    else:
        end_session = "no_category"

    if "has_sale" in sessions:
        has_sale = sessions["has_sale"]
    else:
        has_sale = None

    if "Object" in sessions["order"]["products"]:
        products_in_shoppingcart = []
        for object in sessions["order"]["products"]:
            products_in_shoppingcart.append(object)
    else:
        products_in_shoppingcart = "0"

    print(id, start_session, end_session, has_sale, products_in_shoppingcart)
    productsql = "INSERT INTO sessions(_id, start_session, end_session, has_sale, products_in_shoppingcart) VALUES (\"{}\", \"{}\", \"{}\", {}, {}".format(str(id), str(start_session), str(end_session), bool(has_sale), int(products_in_shoppingcart))
    #print(productsql)
    #executesql(productsql, sqldb)