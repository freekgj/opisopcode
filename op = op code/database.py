def main():
    import pymysql
    import pymysql.cursors
    mydb = pymysql.connect(host='127.0.0.1',
                          user='root',
                          passwd='zaq1xsw2',
                          database="op_is_op_database"
                          )

    mycursor = mydb.cursor()

    print("choose what to do")
    print("option1: create table")
    print("option2: sadfsadf")
    answer = input("option:")
   # if answer == 1:
        #mycursor.execute("CREATE TABLE {}".format())