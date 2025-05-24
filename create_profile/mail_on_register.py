import smtplib

def send_registration_mail(email, name, slno):
    subject = "Welcome to TO-DO_LIST - Registration Successful"
    message = f"""Hi {name},

Thank you for registering with TO-DO_LIST.
Your profile has been created successfully!

Here is your unique ID: {slno}

You can use this unique ID to log in and add your schedules.

Regards,
Team TO-DO_LIST
"""
    sender_email = "aayushtalukdar@gmail.com"
    sender_password = "jage ssmf vnig ccib"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, f"Subject: {subject}\n\n{message}")
        print("Your Unique ID to log-in in TO-DO_LIST has been sent to your email address!")
    except Exception:
        print("Failed to send registration confirmation email. Please try again later!")