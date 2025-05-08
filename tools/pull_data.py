#pull_data.get_data_profile(con, cur, unique_id) will pull the data like name, phone, mail address

def get_data_profile(cur, unique_id):
    from tools import exists
    
    if exists.profile_exists(cur, unique_id):
        query = f"select * from profile where SlNo={unique_id}"
        cur.execute(query)
        data = cur.fetchone()

        name = data[1]
        phone = data[2]
        mail = data[3]

        return (name, phone, mail)

    else:
        return False