from pymongo import MongoClient
client = MongoClient('localhost', 27017)

db = client.op_is_op_data

products = db.products.find()
sessions = db.sessions.find()
visitors = db.sessions.find()
category1 = 'price'
subcategory1 = 'selling_price'

def getpriceproduct(file, subject1, subject2):
    for word in file:
        if subject1 in word:
            subject = (word[subject1])
            if subject2 in subject:
                return subject[subject2]

def getfirstproductwithX(subject, letter):
    for word in subject:
        if 'name' in word:
            catogory = word['name']
            if catogory[0] == letter:
                return catogory

#def gemiddelde_prijs_alle_producten():


for word in products:
    print(word)


getpriceproduct(products, category1, subcategory1)
#getfirstproductwithX(products, "h")
#gemiddelde_prijs_alle_producten()
