import smtplib

def send_registration_mail(email, name, slno):
    subject = "Welcome to PlanBee – Registration Successful"
    message = f"""
Hello {name},

Thank you for registering with PlanBee!
Your profile has been created successfully.

Your PlanBee Unique ID: {slno}

You can use this ID to log in and start adding your schedules.


Best regards,  
The PlanBee Team
"""
    sender_email = "aayushtalukdar@gmail.com"
    sender_password = "jage ssmf vnig ccib"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, f"Subject: {subject}\n\n{message}")
        print("📧 Your Unique ID to log-in in TO-DO_LIST has been sent to your email address!")
    except Exception:
        print("❌ Failed to send registration confirmation email. Please try again later!")