from database import connectmongo
from database import connectsql
from database import push
from models_products import getproducts
from models_products import saveproduct

def execute_products():

    dbmongo = connectmongo()
    dbsql = connectsql()

    products = getproducts(dbmongo)

    for product in products:
        saveproduct(product, dbsql)

    productsql = '''INSERT INTO products (
                                                _id, 
                                                stock, 
                                                brand, 
                                                category,  
                                                gender, 
                                                herhaalaankopen, 
                                                selling_price) VALUES (%s, %s, \"%s\", \"%s\", \"%s\", %s, %s)'''

    push(productsql, dbsql)