from database import connectmongo
from database import connectsql
from models import getproducts
from models import saveproduct


dbmongo = connectmongo()
dbsql = connectsql()

products = getproducts(dbmongo)  #database_mongo.products.find()

for product in products:
    saveproduct(product, dbsql)