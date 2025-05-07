#exists.data_exists(con, cur, unique_id) will check if the user exists or not.

def profile_exists(cur, unique_id):
    query = f'select * from profile where SlNo={unique_id}'
    cur.execute(query)
    data = cur.fetchone()
    if cur.rowcount == 0:
        return False
    
    else:
        return True
    