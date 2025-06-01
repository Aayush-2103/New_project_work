#the nervous system of the to_do list

def control():
    import mysql.connector as mysql
    import os, sys, subprocess, psutil
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(base_dir)

    import login.main
    import schedules.main, schedules.delete_upcoming_events, schedules.view_schedules, schedules.edit_schedules, create_profile.index_1
    import tools.connection

    #connection object
    con = mysql.connect(
        host = 'localhost',
        user = 'root',
        password = 'tiger',
    )

    #cursor object
    cur = con.cursor()
    cur.execute("create database if not exists userpf")
    cur.execute("Use userpf")

    #system to create the two tables "profile" and "events":
    #creating table profile
    cur.execute('''
                create table if not exists profile(
                SLNO int primary key,
                NAME varchar(48),
                PHONE char(10) unique,
                EMAIL_ID varchar(100) unique
                )''')

    #creating table events
    cur.execute('''
                create table if not exists events(
                SLNO varchar(100) primary key,
                TASK_NAME varchar(40),
                DATE_AND_TIME datetime,
                NOTE varchar(500) default "--",
                ALERT_TIME time,
                notify_time datetime
                )''')

    con.commit()

    if tools.connection.is_connected():

        while True:
            print(f'Welcome\n')
            print(f'1. Create Profile')
            print(f'2. Login')
            print(f'3. Exit')

            print()
            option = input('Enter your choice:- ')        
            if option == '1':
                #create profile function call
                create_profile.index_1.create_profile(con, cur)

            elif option == '2':
                #login function call
                response, uid = login.main.lets_log_in(cur)
                if response:                #successfull login
                    notify_mech = subprocess.Popen(["start", "cmd", "/k","python notification/main.py", str(uid)], shell=True)
                    while True:
                        #if login successfull then further ask the user for more options
                        print(f'1. Create new schedule')
                        print(f'2. View all schedules')
                        print(f'3. Edit schedule')
                        print(f'4. Delete upcoming schedule')
                        print(f'5. Logout')
                        print()

                        option = input('Enter your choice:- ')
                        if option == '1':
                            schedules.main.make_schedule(con, cur, uid)
                            print()
                            print('Schedule create successfully')
                            print()

                        elif option == '2':
                            schedules.view_schedules.view(cur, uid)
                            print()

                        elif option == '3':
                            schedules.edit_schedules.make_edits(con, cur, uid)
                    
                        elif option == '4':
                            schedules.delete_upcoming_events.delete_events(cur, uid)
                            print()

                        elif option == '5':
                            print()
                            for process in psutil.process_iter(['pid', 'name', 'cmdline']):
                                if 'python' in process.info['name'] and 'notification/main.py' in str(process.info['cmdline']):
                                    process.kill()
                                    break
                            os.system("taskkill /f /im cmd.exe >nul >2&1")
                            break

                        else:
                            print('Select from the given options')


            elif option == '3':
                print('Thank you for using TO-DO_LIST! Have a great day ahead! 😀')
                print()
                break

            else:
                print('Select from the given options.')
                print()

    else:
        print('Please make sure your device is connected to INTERNET.')
        print()

control()