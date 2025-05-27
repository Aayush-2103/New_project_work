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
        slno = str(uid)+'_'+str(num)

        insert_query = "INSERT INTO events VALUES ('%s', '%s', '%s', '%s', '%s')"%(slno, task_name, date_time, note, alert)
        cur.execute(insert_query)
        con.commit()