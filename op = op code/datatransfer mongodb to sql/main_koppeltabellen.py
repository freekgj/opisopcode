from database import connectmongo
from database import connectsql
from models_koppeltabellen import getsessions
from models_koppeltabellen import getvisitors
from models_koppeltabellen import save_order
from models_koppeltabellen import save_buids

def execute_koppeltabel_order():

    dbmongo = connectmongo()
    dbsql = connectsql()

    sessions = getsessions(dbmongo)  #database_mongo.products.find()

    for session in sessions:
        save_order(session, dbsql)

def execute_koppeltabel_buids():
    dbmongo = connectmongo()
    dbsql = connectsql()

    visitors = getvisitors(dbmongo)

    for visitor in visitors:
        save_buids(visitor, dbsql)