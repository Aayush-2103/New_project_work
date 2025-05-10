#feature to let the user see all his past and futurere schedules

def view(cur, uid):
    query = 'select * from events where SlNo like "%s"'%('%'+str(uid)+'%')
    cur.execute(query)

    data = cur.fetchall()
    n = cur.rowcount
    for i in range(n):
        print(str(i+1)+')', data[i][0], '|', data[i][1], '|', data[i][2], '|', data[i][3])