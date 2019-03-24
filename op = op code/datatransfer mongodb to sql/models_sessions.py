from database import executesql

def getsessions(database):
    return database.sessions.find()

def change_high_comma(item):
    if type(item) == str:
        if "'" in item or '"' in item:
            item = item.replace("'", "")
            item = item.replace('"', "")
            return item
        return item
    return item

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

    sessionsql = '''INSERT INTO sessions (
                                _id,
                                start_session, 
                                end_session, 
                                buid) 
                                VALUES (\"%s\", \"%s\", \"%s\", \"%s\")'''

    row_data = [id, start_session, end_session, buid]
    row_data_complete = []

    for item in row_data:
        checked_item = change_high_comma(item)
        row_data_complete.append(checked_item)

    executesql(sessionsql, row_data_complete, sqldb)