
def transfer(catogory1, catogory2, catogory3, catogory4, catogory5, catogory6, catogory7):
    import pymysql.cursors
    mydb = pymysql.connect(host='127.0.0.1',
                           user='root',
                           passwd='zaq1xsw2',
                           database="op_is_op_database"
                           )

    mycursor = mydb.cursor()
    #mycursor.execute("SHOW TABLES")
    #mycursor.execute("CREATE TABLE products (_id INT(15), brand VARCHAR(20), category VARCHAR(50), fast_mover BOOLEAN, gender varchar(10), herhaalaankopen BOOLEAN, selling_price INT(15))")

    insert_product_data = "INSERT INTO products (_id, brand, category, fast_mover, gender, herhaalaankopen, selling_price) VALUES %s, %s, %s, %s, %s, %s, $s)"

    product = (catogory1, catogory2, catogory3, catogory4, catogory5, catogory6, catogory7)

    mycursor.execute(insert_product_data, product)

    mydb.commit()


