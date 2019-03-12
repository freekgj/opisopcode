from database import connectmongo
from database import connectsql
from models_visitors import getvisitors
from models_visitors import savevisitor

def execute_visitors():

    dbmongo = connectmongo()
    dbsql = connectsql()

    visitors = getvisitors(dbmongo)  #database_mongo.products.find()

    for visitor in visitors:
        savevisitor(visitor, dbsql)