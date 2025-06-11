#system to send otp in mail for log in

def mail(name, phone, receiver, count):
    import os, sys, random
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(base_dir)
    
    from Mail import otp_mail, time_exp

    from datetime import datetime
    import connection

    if connection.is_connected():
        #generate otp
        otp = ''
        for i in range(6):
            otp += str(random.randint(0,9))

        otp = int(otp)

        print('⏳ Loading...')

        #sending the mail
        otp_mail.otp_login(name, phone, receiver, otp)

        time = time_exp.exp_time()          #expiry time

        #user input for otp
        print()
        print(f'📧 OTP sent to the registered mail id: {receiver}')        
        print(f'⏰ Your OTP is valid till {time}')
        print(f'🔄 You can resend the otp more {3-count} times by entering "resend".')
        user = input('Enter otp: ')
        print()

        current = datetime.now().strftime('%H:%M, %d %B, %Y')
        if current > time:
            print('⌛ OTP Expired !!!')
            return False

        if user.lower() == 'resend':
            if count<3:
                count+=1
                return mail(name, phone, receiver, count)
            
            else:
                print('🚫 No more chances for now.')
                return False

        elif user == str(otp):
            return True
        
        elif user != str(otp):
            print('❌ Invalid OTP !!!')
            return False

    else:
        print(f'🌐 Please ensure your device is connected with an active internet connection.')
        return False
