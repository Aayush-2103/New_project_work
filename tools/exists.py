#exists.data_exists(con, cur, unique_id) will check if the user exists or not.

def profile_exists(cur, unique_id):
    query = 'select * from profile where SlNo=%s'
    cur.execute(query, (unique_id, ))
    data = cur.fetchall()
    if data:
        return True
    
    else:
        return False