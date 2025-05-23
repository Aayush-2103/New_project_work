#the nervous system of the to_do list

def control():
    import mysql.connector as mysql
    import os, sys
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(base_dir)

    import login.main
    import schedules.main, schedules.view_schedules, schedules.edit_schedules, create_profile.index_1
    
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
            if response:
                while True:
                    #if login successfull then further ask the user for more options
                    print(f'1. Create new schedule')
                    print(f'2. View all schedules')
                    print(f'3. Edit schedule')
                    print(f'4. Logout')
                    print()

                    option = input('Enter your choice:- ')
                    if option == '1':
                        schedules.main.make_schedule(con, cur, uid)
                        print()
                        print('Schedule create successfully')

                    elif option == '2':
                        schedules.view_schedules.view(cur, uid)
                        print()

                    elif option == '3':
                        schedules.edit_schedules.make_edits(con, cur, uid)

                    elif option == '4':
                        print()
                        break

                    else:
                        print('Select from the given options')


        elif option == '3':
            print('Goodbye')
            print()
            break

        else:
            print('Select from the given options.')
            print()

control()