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
    return database.products.find()

def saveproduct(product, sqldb):
    if "_id" in product and product["_id"].isdigit == True:
        id = product["_id"]
    else:
        id = int(get_unique_id())

    if "brand" in product:
        brand = product["brand"]
    else:
        brand = "no_brand"

    if "category" in product:
        categoryofproduct = product["category"]
    else:
        categoryofproduct = "no_category"

    if "fast_mover" in product:
        fast_mover = product["fast_mover"]
    else:
        fast_mover = None

    if "gender" in product:
        gender = product["gender"]
    else:
        gender = "0"

    if "herhaalaankopen" in product:
        herhaalaankopen = product["herhaalaankopen"]
    else:
        herhaalaankopen = 0

    if "price" in product:
        selling_price = product["price"]["selling_price"]
    else:
        selling_price = 0

    print(product)
    if "stock" in product["properties"]:
        stock = product["properties"]["stock"]
    else:
        stock = 0

    print(id, stock, brand, categoryofproduct, fast_mover, gender, herhaalaankopen, selling_price)
    productsql = "INSERT INTO products (_id, stock, brand, category, fast_mover, gender, herhaalaankopen, selling_price) VALUES ({}, {}, \"{}\", \"{}\", {}, \"{}\", {}, {})".format(int(id), int(stock), str(brand), str(categoryofproduct), bool(fast_mover), str(gender), bool(herhaalaankopen), int(selling_price))
    #print(productsql)
    #executesql(productsql, sqldb)