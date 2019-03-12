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

def getSQLdata(statement,sqldb):
    mycursor = sqldb.cursor()
    mycursor.execute(statement)
    return mycursor.fetchall()
