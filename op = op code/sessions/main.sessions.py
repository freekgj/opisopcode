from database import connectmongo
from database import connectsql
from models.sessions import getsessions
from models.sessions import savesession


dbmongo = connectmongo()
dbsql = connectsql()

sessions = getsessions(dbmongo)  #database_mongo.products.find()

for session in sessions:
    savesession(session, dbsql)