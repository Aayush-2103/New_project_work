#to edit schedules

def make_edits(con, cur, uid):
    #helping him to search
    from datetime import timedelta

    print()
    print('🔍 Enter any part of the task name you remember.')
    search = input()
    print()

    query = 'select * from events where task_name like "%s" and slno like "%s"'%('%'+search+'%', '%'+str(uid)+'%')
    cur.execute(query)
    data = cur.fetchall()
    n = cur.rowcount

    if n!=0:
        #search results
        all_codes = [data[i][0] for i in range(n)]
        for i in range(n):
            print(str(i+1)+')', '|', data[i][1], '|', data[i][2], '|', data[i][3], '|', data[i][4])

        print()
        option = int(input('Si.No of the task you want to edit:- '))
        print()
        if option in range(1,n+1):
            code = all_codes[option-1]

            while True:
                print(f'1. Task name')
                print(f'2. Date and time')
                print(f'3. Note')
                print(f'4. Alert time')
                print(f'5. Exit')
                print()
                choice = int(input('Which field you want to edit:- '))
                print()

                if choice == 1:
                    task_name = input('Task name:- ')
                    query = 'update events set task_name="%s" where slno="%s"'%(task_name, code)
                    cur.execute(query)
                    con.commit()
                    print()
                    print('✅ Updates saved successfully.')
                    
                elif choice == 2:
                    print('Date & time in (yyyy-mm-dd 17:45) format')
                    date_time = input()
                    query = 'update events set date_and_time="%s" where slno="%s"'%(date_time, code)
                    cur.execute(query)
                    con.commit()

                    #changing the notification date and time
                    query = 'select * from events where slno = "%s"'%(code)
                    cur.execute(query)
                    data = cur.fetchone()
                    date_and_time = data[2]
                    alert_time = str(data[4]).split(':')
                    hrs = int(alert_time[0])
                    mins = int(alert_time[1])

                    notify_time = date_and_time - timedelta(hours=hrs,  minutes=mins)
                    query = 'update events set notify_time = "%s" where slno="%s"'%(notify_time, code)
                    cur.execute(query)
                    con.commit()

                    print()
                    print('✅ Updates saved successfully.')
                    
                elif choice == 3:
                    print('NOTE (Optional):- ')
                    note = input()
                    if note == '':
                        note = '--'

                    query = 'update events set note="%s" where slno="%s"'%(note, code)
                    cur.execute(query)
                    con.commit()
                    print()
                    print('✅ Updates saved successfully.')
                    
                elif choice == 4:
                    alert = (input('Alert time(in HH:MM format):- '))
                    query = 'update events set alert_time="%s" where slno="%s"'%(alert, code)
                    cur.execute(query)
                    con.commit()

                    #changing the notification date and time
                    query = "select * from events where slno = '%s'"%(code)
                    cur.execute(query)
                    data = cur.fetchone()
                    date_and_time = data[2]
                    time_split = alert.split(':')
                    hrs = int(time_split[0])
                    mins = int(time_split[1])

                    notify_time = date_and_time - timedelta(hours=hrs, minutes=mins)
                    query = "update events set notify_time = '%s' where slno = '%s'"%(notify_time, code)
                    cur.execute(query)
                    con.commit()

                    print()
                    print('✅ Updates saved successfully.')

                elif choice == 5:
                    break

                else:
                    print('⚠️ Please select from the option given.')

                print()

        else:
            print('❌ Invalid option number.')
            print('❌ Process Terminated !!!')
            print()

    else:
        print('⚠️ No records to edit.')