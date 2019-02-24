from database import connectmongo
from database import connectsql
from models.visitors import getvisitors
from models.visitors import savevisitor


dbmongo = connectmongo()
dbsql = connectsql()

visitors = getvisitors(dbmongo)  #database_mongo.products.find()

for visitor in visitors:
    savevisitor(visitor, dbsql)