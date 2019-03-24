from database import connectmongo
from database import connectsql
from database import push
from models_visitors import getvisitors
from models_visitors import savevisitor

def execute_visitors():

    dbmongo = connectmongo()
    dbsql = connectsql()

    visitors = getvisitors(dbmongo)

    for visitor in visitors:
        savevisitor(visitor, dbsql)

    visitorsql = '''INSERT INTO visitors (
                                            visitor_ID, 
                                            count_overall_products,
                                            first_order, 
                                            latest_order, 
                                            latest_activity) 
                                            VALUES (\"%s\", \"%s\", \"%s\", \"%s\", \"%s\")'''

    push(visitorsql, dbsql)