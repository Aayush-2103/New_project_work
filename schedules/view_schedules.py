#feature to let the user see all his past and future schedules

def view(cur, uid):
    query = 'select * from events where SlNo like "%s"'%('%'+str(uid)+'%')
    cur.execute(query)

    data = cur.fetchall()
    n = cur.rowcount
    if n == 0:
        print("No schedule found!📌")
        return
    for i in range(n):
        print(str(i+1)+')', data[i][0], '|', data[i][1], '|', data[i][2], '|', data[i][3])