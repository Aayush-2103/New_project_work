#to edit schedules

def make_edits(con, cur, uid):
    #helping him to search
    print()
    print('Enter any part of the task name you remember.')
    search = input()
    print()

    query = 'select * from events where task_name like "%s" and slno like "%s"'%('%'+search+'%', '%'+str(uid)+'%')
    cur.execute(query)
    data = cur.fetchall()
    n = cur.rowcount

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
                print('Updates saved successfully.')
                
            elif choice == 2:
                print('Date & time in (yyyy-mm-dd 17:45) format')
                date_time = input()
                query = 'update events set dateandtime="%s" where slno="%s"'%(date_time, code)
                cur.execute(query)
                con.commit()
                print()
                print('Updates saved successfully.')
                
            elif choice == 3:
                print('NOTE (Optional):- ')
                note = input()
                if note == '':
                    note = '--'

                query = 'update events set note="%s" where slno="%s"'%(note, code)
                cur.execute(query)
                con.commit()
                print()
                print('Updates saved successfully.')
                
            elif choice == 4:
                alert = int(input('Alert time(in mins):- '))
                query = 'update events set alert_time=%s where slno="%s"'%(alert, code)
                cur.execute(query)
                con.commit()
                print()
                print('Updates saved successfully.')

            elif choice == 5:
                break

            else:
                print('Please select from the option given.')

            print()

    else:
        print('Invalid option number.')
        print('Process Terminated !!!')
        print()