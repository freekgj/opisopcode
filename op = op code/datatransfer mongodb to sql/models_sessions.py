from database import executesql

count = 0
row_data = []
row_count = 0

def getsessions(database):
    return database.sessions.find()

def savesession(session, sqldb):
    if "_id" in session:
        id = str(session["_id"])
    else:
        return

    if ("buid" in session) and session["buid"] != None:
        buid = str(session["buid"][0])
    else:
        return

    if "session_start" in session:
        start_session = str(session["session_start"])
    else:
        start_session = ""

    if "session_end" in session:
        end_session = str(session["session_end"])
    else:
        end_session = ""

    global count
    count += 1

    global row_data
    row_data.append((id, start_session, end_session, buid))

    if count == 1000:
        sessionsql = '''INSERT INTO sessions (
                            _id,
                            start_session, 
                            end_session, 
                            buid) 
                            VALUES (\"%s\", \"%s\", \"%s\", \"%s\")'''
        global row_count
        row_count += 1
        print("session - row " + str(row_count))
        executesql(sessionsql, row_data, sqldb)
        row_data = []
        global count
        count = 0