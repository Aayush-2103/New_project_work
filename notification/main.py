def notify(cur, unique_id):
    import os, sys
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(base_dir)

    from datetime import datetime
    import tools.pull_data, tools.Mail.notify_mail
   
    task_name, date_time, note, notify_time = tools.pull_data.get_event_info(cur, unique_id)

    if task_name:
        #personal info
        info = tools.pull_data.get_data_profile(cur, int(unique_id))
        user_name = info[0]
        user_mail = info[2]

        now = datetime.now().strftime('%Y-%m-%d %H:%M')

        if now == notify_time:                
            tools.Mail.notify_mail.notification_mail(task_name, date_time, note, user_name, user_mail)


from datetime import datetime
past = datetime.now().strftime('%Y-%m-%d %H:%M')
while True:
    import sys
    import mysql.connector as mysql

    con = mysql.connect(
        host = 'localhost',
        user = 'root',
        password = 'tiger',
        database = 'userpf' 
    )
    cur = con.cursor()

    unique_id = sys.argv[1]

    now = datetime.now().strftime('%Y-%m-%d %H:%M')
    if past!=now:  #radar check after every minute
        notify(cur, unique_id)
        past = now