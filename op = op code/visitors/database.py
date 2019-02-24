from pymongo import MongoClient
import pymysql

def connectmongo():
    client = MongoClient('localhost', 27017)
    database_mongo = client.op_is_op_data
    return database_mongo

def connectsql():
    mydb = pymysql.connect(host='127.0.0.1',
                           user='root',
                           passwd='zaq1xsw2',
                           database="op_is_op_database"
                           )
    return mydb

def executesql(statement, sqldb):
    mycursor = sqldb.cursor()
    #mycursor.execute("SHOW TABLES")
    #mycursor.execute("CREATE TABLE products (_id serial primary key, brand VARCHAR(20), category VARCHAR(80), fast_mover BOOLEAN, gender varchar(25), herhaalaankopen BOOLEAN, selling_price INT(15))")
    mycursor.execute(statement)

    sqldb.commit()