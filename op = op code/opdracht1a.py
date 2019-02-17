from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.op_is_op_data

products = db.products.find()
sessions = db.sessions.find()
visitors = db.sessions.find()
category1 = 'price'
subcategory1 = 'selling_price'

def get_first_product_price(file, subject1, subject2):
    for word in file:
        if subject1 in word:
            subject = (word[subject1])
            if subject2 in subject:
                return subject[subject2]

def get_first_product_with_X(subject, letter):
    for word in subject:
        if 'name' in word:
            catogory = word['name']
            if catogory[0] == letter:
                return catogory

def gemiddelde_prijs_alle_producten(file):
    listprice = []
    total = 0
    for word in file:
        if "price" in word:
            price = (word["price"])
            if "selling_price" in price:
                listprice.append(price["selling_price"])
    for product in listprice:
        total += product
    avg = total / len(listprice)
    return avg



print(get_first_product_price(products, category1, subcategory1))
print(get_first_product_with_X(products, "h"))
print(gemiddelde_prijs_alle_producten(products))

