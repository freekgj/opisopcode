from pymongo import MongoClient
counter = 0
client = MongoClient('localhost', 27017)
database_mongo = client.op_is_op_data
products = database_mongo.products.find()

for product in products:
    for catogory in product:
        if product["_id"] != "":
            id = product["_id"]
        else:
            id = None

        if product["brand"] != "":
            brand = product["brand"]
        else:
            brand = None

        if product["category"] != "":
            catogoryofproduct = product["category"]
        else:
            catogoryofproduct = None

        if product["fast_mover"] != "":
            fast_mover = product["fast_mover"]
        else:
            fast_mover = None

        if product["gender"] != "":
            gender = product["gender"]
        else:
            gender = None

        if product["herhaalaankopen"] != "":
            herhaalaankopen = product["herhaalaankopen"]
        else:
            herhaalaankopen = None

        if product["price"]["selling_price"] != "":
            selling_price = product["price"]["selling_price"]
        else:
            selling_price = None

    counter +=1
    print(counter)
    import database
    database.transfer(id, brand, catogoryofproduct, fast_mover, gender, herhaalaankopen, selling_price)

