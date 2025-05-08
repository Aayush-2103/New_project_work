#just to make new schedules.

def make_schedule(con, cur):
    import os, sys
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(base_dir)

    from tools import exists
    
    print()
    uid = int(input('Enter unique id:- '))
    print()
    if exists.profile_exists(cur, uid):
        task_name = input('Task name:- \t\t\t\t')

        print('Date & time in (yyyy-mm-dd 17:45) format')
        date_time = input()

        print('NOTE (Optional):- ')
        note = input()
        if note == '':
            note = '--'
            
        alert = int(input('Alert time(in mins):- '))

        query = "insert into events values (%s, '%s', '%s', '%s', %s)"%(uid, task_name, date_time, note, alert)

        cur.execute(query)
        con.commit()        

    else:
        print(f'User id:{uid} is not available in database.')
