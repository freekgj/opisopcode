from database import connectmongo
from database import connectsql
from models_sessions import getsessions
from models_sessions import savesession

def execute_sessions():

    dbmongo = connectmongo()
    dbsql = connectsql()

    sessions = getsessions(dbmongo)  #database_mongo.products.find()

    for session in sessions:
        savesession(session, dbsql)