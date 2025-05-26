def notify(cur, unique_id):
    import os, sys
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(base_dir)

    from datetime import datetime
    import tools.pull_data, tools.Mail.notify_mail
   
    #check every minute to send notification mail if any
    past = datetime.now().strftime('%Y-%m-%d %H:%M')
    while True:
        now = datetime.now().strftime('%Y-%m-%d %H:%M')
        if past != now:       #radar checks
            past = now

            task_name, date_time, note, notify_time = tools.pull_data.get_event_info(cur, unique_id)

            if task_name:
                #personal info
                info = tools.pull_data.get_data_profile(cur, unique_id)
                user_name = info[0]
                user_mail = info[2]

                print(now)

                if now == notify_time:
                    #notification sending mail has to be done.
                    tools.Mail.notify_mail.notification_mail(task_name, date_time, note, user_name, user_mail)
        