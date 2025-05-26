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
    
def get_event_info(cur, unique_id):
    #getting the event info of the event whose mail has to be sent
    
    from datetime import datetime, timedelta
    import pytz

    tz = pytz.timezone('Asia/Kolkata')
    now = datetime.now(tz)
    now_format = now.strftime("%Y-%m-%d %H:%M:%S")

    #getting the nearest event alert time
    query = "select * from events where dateandtime > '%s' and slno like '%s'"%(now_format, unique_id+'%')
    cur.execute(query)
    data = cur.fetchone()

    if cur.rowcount == 1:
        task_name = data[1]
        date_time = data[2]
        note = data[3]
        alert_time = str(data[-1])
        alert_time = alert_time.split(':')
        
        #time in which notification should be sent
        notify_time = date_time - timedelta(
                        hours=int(alert_time[0]),
                        minutes=int(alert_time[1]),
                        seconds=int(alert_time[2])
        )
        notify_time = notify_time.strftime('%Y-%m-%d %H:%M')

        return task_name, date_time, note, notify_time

    else:
        return False, False, False, False