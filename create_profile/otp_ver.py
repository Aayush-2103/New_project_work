import random
import smtplib
from datetime import datetime, timedelta
import pytz




# Dictionary to store OTP details
otp_data = {}



# Function to calculate OTP expiry time
def calculate_expiry_time():
    #Calculate and return the OTP expiry time in the desired format.
    tz = pytz.timezone('Asia/Kolkata')  # Set timezone to Asia/Kolkata
    now = datetime.now(tz)  # Get current time in the specified timezone
    expiry_time = now + timedelta(minutes=10)  # Add 10 minutes to the current time
    formatted_time = expiry_time.strftime('%H:%M; %d %B, %Y')  # Format the expiry time
    return formatted_time, expiry_time



# Function to send OTP
def send_otp(name, email):
    otp = random.randint(100000, 999999)
    subject = "One-Time Password (OTP) for your PlanBee profile"
    formatted_expiry_time, expiry_time = calculate_expiry_time()
    # A unique footer to each email to avoid Gmail clipping
    unique_footer = f"\n\n---\nUnique OTP_ID: {random.randint(1000000000, 9999999999)}\n"
    message = f"""
Hello {name},

Your One-Time Password (OTP) for verifying your email with PlanBee is: {otp}

This OTP is valid for 10 minutes, until {formatted_expiry_time}.

If you did not request this OTP, please ignore this email.

Best regards,  
The PlanBee Team
{unique_footer}
"""

    sender_email = "aayushtalukdar@gmail.com"
    sender_password = "jage ssmf vnig ccib"


    # Send the email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, f"Subject: {subject}\n\n{message}")
        


        # Initialize or update OTP details
        if email not in otp_data:
            otp_data[email] = {
                "otp": otp,
                "expires_at": expiry_time,  # Store the raw expiry time
                "resend_count": 0
            }
        else:
            otp_data[email]["otp"] = otp
            otp_data[email]["expires_at"] = expiry_time



        # Increment resend count
        remaining_attempts = 3 - otp_data[email]["resend_count"]
        print(f"📧 An OTP has been sent to your email. It is valid until {formatted_expiry_time}.")
        print(f"🔄 You can resend the OTP {remaining_attempts} more time(s).")
        return otp
    
        
    except Exception:
        print("❌ Failed to send OTP. Please check your email address and try again!")
        return None



# Function to validate OTP  
def validate_otp(email, user_otp):
    if email not in otp_data:
        print("❌ No OTP found for this email. Please request a new OTP.")
        return False

    details = otp_data[email]
    tz = pytz.timezone('Asia/Kolkata')
    now = datetime.now(tz)

    if now > details["expires_at"]:
        print("⌛ OTP has expired. Please request a new OTP.")
        return False

    if str(details["otp"]) != str(user_otp):
        return False

    return True




# Function to resend OTP
def resend_otp(name, email):
    if email in otp_data and otp_data[email]["resend_count"] >= 3:
        print("🚫 You have reached the maximum OTP resend limit.")
        return None

    otp_data[email]["resend_count"] += 1
    print("🔄 Resending OTP...")
    return send_otp(name, email)