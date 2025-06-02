#just to make new schedules.

def make_schedule(con, cur, uid):
    import os, sys
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(base_dir)

    from tools import exists
    from datetime import timedelta
    
    print()
    if exists.profile_exists(cur, uid):
        task_name = input('Task name:- ')

        print('📅 Date & time in (yyyy-mm-dd 17:45) format')
        date_time = input()

        print('📝 NOTE (Optional):- ')
        note = input()
        if note == '':
            note = '--'
            
        alert = str(input('⏰ Alert time(in HH:MM format):- '))

        #getting the count of events by that user
        query = 'select count(*) from events where slno like %s'
        cur.execute(query, ('%' + str(uid) + '%',))
        data = cur.fetchone()
        num = data[0] + 1
        slno = str(uid)+'_'+str(num)

        try:
            insert_query = "INSERT INTO events VALUES (%s, %s, %s, %s, %s, default)"
            cur.execute(insert_query, (slno, task_name, date_time, note, alert))
            con.commit()

            #retrieve date_and_time and alert_time
            query = "select * from events where slno = '%s'"%(slno)
            cur.execute(query)
            data = cur.fetchone()
            date_and_time = data[2]
            time_split = alert.split(':')
            hrs = int(time_split[0])
            mins = int(time_split[1])

            notify_time = date_and_time - timedelta(hours=hrs, minutes=mins)
            notify_time.strftime('%Y-%m-%d %H:%M')

            query = "update events set notify_time = '%s' where slno = '%s'"%(notify_time, slno)
            cur.execute(query)
            con.commit()
            
        except:
            print()
            print('⚠️ Please check the input format once again and try again.')
            return make_schedule(con, cur, uid)