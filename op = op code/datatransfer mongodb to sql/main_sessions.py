from database import connectmongo
from database import connectsql
from database import push
from models_sessions import getsessions
from models_sessions import savesession

def execute_sessions():

    dbmongo = connectmongo()
    dbsql = connectsql()

    sessions = getsessions(dbmongo)

    for session in sessions:
        savesession(session, dbsql)

    sessionsql = '''INSERT INTO sessions (
                                _id,
                                start_session, 
                                end_session, 
                                buid) 
                                VALUES (\"%s\", \"%s\", \"%s\", \"%s\")'''

    push(sessionsql, dbsql)