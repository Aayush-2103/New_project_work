#to send otp into the given mail address

def otp_login(name, phone, receiver, otp):
    import smtplib, os, sys
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(base_dir)

    from email.message import EmailMessage
    from Mail import time_exp

    sender_mail = 'aayushtalukdar@gmail.com' 
    password = 'jage ssmf vnig ccib'            #security key of gmail two step-verification

    msg = EmailMessage()

    #masking the phone number
    phone = '*'*6 + str(phone)[6:]

    #getting the expiry_time
    time = time_exp.exp_time()

    message = f'''
Hello {name},

Your One-Time Password (OTP) for logging into your PlanBee account (registered phone: {phone}) is:

🔐 OTP: {otp}

This code is valid for the next 10 minutes, until {time}.

Please do not share this code with anyone.
If you did not request this login, please ignore this email.

Best regards,  
The PlanBee Team
                '''
    
    msg.set_content(message)

    msg['Subject'] = 'Log in OTP'
    msg['From'] = sender_mail
    msg['To'] = receiver

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_mail, password)
        smtp.send_message(msg)
