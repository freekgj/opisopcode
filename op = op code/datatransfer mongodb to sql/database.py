from pymongo import MongoClient
import pymysql

row_data = []
row_count = 0
count = 0

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

def executesql(statement, data, sqldb):
    global row_data
    row_data.append(data)
    global count
    count += 1
    if count == 1000:
        push(statement, sqldb)
        count = 0
        global row_count
        row_count += 1
        print("{} - row ".format(statement[12]) + str(row_count))

def push(statement, sqldb):
    global row_data
    mycursor = sqldb.cursor()
    mycursor.executemany(statement, row_data)
    sqldb.commit()
    row_data = []