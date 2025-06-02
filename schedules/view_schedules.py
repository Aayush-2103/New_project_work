#feature to let the user see all his past and future schedules

def view(cur, uid):
    query = 'select * from events where SlNo like "%s"'%('%'+str(uid)+'%')
    cur.execute(query)

    data = cur.fetchall()
    n = cur.rowcount
    if n != 0:
        print()
        print('SlNo', 'Event Code', '|', 'Task Name', '|', 'Scheduled Date and time', '|', 'NOTE', '|', 'Alert Time','|', 'Notification time')
        for i in range(n):
            print(str(i+1)+')', data[i][0], '|', data[i][1], '|', data[i][2], '|', data[i][3],'|',data[i][4], '|', data[i][5])

    else:
        print('📭 No events to display')