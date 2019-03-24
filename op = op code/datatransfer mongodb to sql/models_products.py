from database import executesql

def getproducts(database):
    return database.products.find()

def change_high_comma(item):
    if type(item) == str:
        if "'" in item or '"' in item:
            item = item.replace("'", "")
            item = item.replace('"', "")
            return item
        return item
    return item

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


    productsql = '''INSERT INTO products (
                                            _id, 
                                            stock, 
                                            brand, 
                                            category,  
                                            gender, 
                                            herhaalaankopen, 
                                            selling_price) VALUES (%s, %s, %s, %s, %s, %s, %s)'''

    row_data = [id, stock, brand, categoryofproduct, gender, herhaalaankopen, selling_price]
    row_data_complete = []

    for item in row_data:
        checked_item = change_high_comma(item)
        row_data_complete.append(checked_item)


    executesql(productsql, row_data_complete, sqldb)