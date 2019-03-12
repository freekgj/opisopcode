from database import executesql

count = 0
row_data = []
row_count = 0

def getproducts(database):
    return database.products.find()

def saveproduct(product, sqldb):
    if "_id" in product:
        id = str(product["_id"])
    else:
        return

    if "brand" in product:
        brand = str(product["brand"])
    else:
        brand = "no_brand"

    if "category" in product:
        categoryofproduct = str(product["category"])
    else:
        categoryofproduct = "no_category"

    if "fast_mover" in product:
        fast_mover = bool(product["fast_mover"])
    else:
        fast_mover = None

    if "gender" in product:
        gender = str(product["gender"])
    else:
        gender = "0"

    if "herhaalaankopen" in product:
        herhaalaankopen = bool(product["herhaalaankopen"])
    else:
        herhaalaankopen = None

    if "price" in product:
        selling_price = int(product["price"]["selling_price"])
    else:
        selling_price = 0

    if "properties" in product and "stock" in product["properties"]:
        stock = int(product["properties"]["stock"])
    else:
        stock = 0

    global count
    count += 1

    global row_data
    row_data.append((id, stock, brand, categoryofproduct, gender, herhaalaankopen, selling_price))

    if count == 1000:
        productsql = '''INSERT INTO products (
                                        _id, 
                                        stock, 
                                        brand, 
                                        category,  
                                        gender, 
                                        herhaalaankopen, 
                                        selling_price) VALUES (\"%s\", %s, \"%s\", \"%s\", \"%s\", %s, %s)'''
        global row_count
        row_count += 1
        print("products - row " + str(row_count))
        executesql(productsql, row_data, sqldb)
        row_data = []
        global count
        count = 0