from database import connectmongo
from database import connectsql
from database import push
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

    ordersql = '''INSERT INTO orders (product_ID, buid) VALUES (\"%s\", \"%s\")'''

    push(ordersql, dbsql)

def execute_koppeltabel_buids():
    dbmongo = connectmongo()
    dbsql = connectsql()

    visitors = getvisitors(dbmongo)

    for visitor in visitors:
        save_buids(visitor, dbsql)

    buidssql = '''INSERT INTO buids (buid, visitor_ID) VALUES (\"%s\", \"%s\")'''

    push(buidssql, dbsql)