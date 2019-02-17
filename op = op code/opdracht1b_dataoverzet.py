from pymongo import MongoClient


client = MongoClient('localhost', 27017)
database_mongo = client.op_is_op_data

products = database_mongo.products.find()


counter = 0

for product in products:
    for catogory in product:
        if catogory == "_id":
            id = product["_id"]
            print(catogory, product["_id"])
        if catogory == "brand":
            brand = product["brand"]
            print(catogory, product["brand"])
        if catogory == "category":
            catogoryofproduct = product["category"]
            print(catogory, product["category"])
        if catogory == "fast_mover":
            fast_mover = product["fast_mover"]
            print(catogory, product["fast_mover"])
        if catogory == "gender":
            gender = product["gender"]
            print(catogory, product["gender"])
        if catogory == "herhaalaankopen":
            herhaalaankopen = product["herhaalaankopen"]
            print(catogory, product["herhaalaankopen"])
        if catogory == "price":
            selling_price = product["price"]["selling_price"]
            print("selling_price", product["price"]["selling_price"])

    break

import database
database.transfer(id, brand, catogoryofproduct, fast_mover, gender, herhaalaankopen, selling_price)