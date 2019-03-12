from database import connectmongo
from database import connectsql
from models_products import getproducts
from models_products import saveproduct

def execute_products():

    dbmongo = connectmongo()
    dbsql = connectsql()

    products = getproducts(dbmongo)  #database_mongo.products.find()

    for product in products:
        saveproduct(product, dbsql)