#just to make new schedules.

def make_schedule(con, cur, uid):
    import os, sys
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(base_dir)

    from tools import exists
    
    print()
    if exists.profile_exists(cur, uid):
        task_name = input('Task name:- ')

        print('Date & time in (yyyy-mm-dd 17:45) format')
        date_time = input()

        print('NOTE (Optional):- ')
        note = input()
        if note == '':
            note = '--'
            
        alert = str(input('Alert time(in HH:MM:SS format):- '))

        #getting the count of events by that user
        query = 'select count(*) from events where slno like %s'
        cur.execute(query, ('%' + str(uid) + '%',))
        data = cur.fetchone()
        num = data[0] + 1

        # Fix SLNO to be int, or change table to accept varchar if you want to use uid_num
        slno = int(str(uid) + str(num))  # Or just use num or uid as int

        # Parse date_time to correct format
        from datetime import datetime, time
        try:
            dt = datetime.strptime(date_time, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Invalid date format. Please use yyyy-mm-dd HH:MM")
            return

        # Convert alert (minutes) to time object
        alert_time = time(hour=alert // 60, minute=alert % 60)

        insert_query = """
            INSERT INTO events (slno, task_name, date_and_time, note, alert_time)
            VALUES (%s, %s, %s, %s, "%s")
        """
        cur.execute(insert_query, (slno, task_name, dt, note, alert_time))
        con.commit()