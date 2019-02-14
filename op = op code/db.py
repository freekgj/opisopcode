import pymysql
import pymysql.cursors
mydb = pymysql.connect(host='127.0.0.1',
                      user='root',
                      passwd='zaq1xsw2',
                      database="op_is_op_database"
                      )

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE products")