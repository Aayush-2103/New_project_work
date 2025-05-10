#the feature to create sucessful log in of the user

def lets_log_in(cur):
    import os, sys
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(base_dir)

    from tools import exists, pull_data
    from tools.Mail import main

    print()
    uid = int(input('Enter unique id:- '))
    print()
    if exists.profile_exists(cur, uid):
        #get the profile data to send mails
        name, phone, mail = pull_data.get_data_profile(cur, uid)

        #after getting these details we will send an otp to the given mail address for sucessful login.
        count = 0

        response = main.mail(name, phone, mail, count)
        if response:
            #log in successfull
            print('Log in successfull.')
            print()
            return True, uid
            
        else:
            print()
            return False

    else:
        print(f'User id:{uid} is not recognised.') 
        return False