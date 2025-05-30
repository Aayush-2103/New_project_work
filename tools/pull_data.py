#pull_data.get_data_profile(con, cur, unique_id) will pull the data like name, phone, mail address

def get_data_profile(cur, unique_id):
    import os,sys
    base_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(base_dir)

    import exists
    
    if exists.profile_exists(cur, int(unique_id)):
        query = "select * from profile where SlNo=%s"
        cur.execute(query, (unique_id, ))
        data = cur.fetchall()

        name = data[0][1]
        phone = data[0][2]
        mail = data[0][3]

        return name, phone, mail

    else:
        return False, False, False
    
def get_event_info(cur, unique_id):
    #getting the event info of the event whose mail has to be sent
    
    from datetime import datetime

    now_format = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    #getting the nearest event alert time
    query = "select * from events where notify_time >= '%s' and slno like '%s' order by notify_time"%(now_format, unique_id+'%')
    cur.execute(query)
    data = cur.fetchall()

    if data:
        task_name = data[0][1]
        date_time = data[0][2].strftime('%Y-%m-%d %H:%M')
        note = data[0][3]
        notify_time = data[0][5].strftime('%Y-%m-%d %H:%M')

        return task_name, date_time, note, notify_time

    else:
        return False, False, False, False