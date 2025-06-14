from create_profile.otp_ver import send_otp, validate_otp, resend_otp



# Function to create a user profile
def create_profile(con, cur):    
    # Name validation
    while True:
        name = input("Enter your name: ").strip()
        if not name:
            print("❗ Name cannot be empty. Please enter your name.")
        elif not all(char.isalpha() or char.isspace() for char in name):
            print("❗ Name can only contain letters and spaces. Please try again.")
        elif len(name) > 50:
            print("❗ Name is too long. Please use fewer than 50 characters.")
        else:
            break



    # Phone number validation
    while True:
        phone = input("Enter your phone number: ").strip()
        if not phone.isdigit():
            print("❗ Phone number should contain only digits.")
        elif len(phone) != 10:
            print("❗ Phone number must be exactly 10 digits.")
        else:
            # Check if the phone number already exists in the database
            query = "SELECT phone FROM profile WHERE phone = %s"
            cur.execute(query, (phone,))
            result = cur.fetchone()
            if result:
                print("⚠️ This phone number is already registered. Please use another number.")
            else:
                break



    # Email validation
    while True:
        email = input("Enter your email: ").strip()
        if not email:
            print("❗ Email cannot be empty. Please enter a valid email.")
        else:
            break

    print('⏳ Sending OTP to your email address...')
    otp = send_otp(name, email)
    if otp is None:
        return



    # OTP validation
    while True:
        user_otp = input("Enter OTP (or type 'resend' to get a new OTP): ").strip().lower()

        if user_otp == "resend":
            if resend_otp(name, email) is None:
                return
            continue

        if validate_otp(email, user_otp):
            break

        print("❌ Invalid or expired OTP! Please try again.")
        return



    query = 'select max(slno) from profile'
    cur.execute(query)
    count = cur.fetchone()

    if count[0] is None:  # If no slno exists in the table
        new_slno = 111111
    else:  # If slno exists, increment the maximum slno by 1
        new_slno = count[0] + 1



    # Insert the new profile into the database
    insert_query = "insert into profile(slno, name, phone, email_id) values (%s, %s, %s, %s)"
    values = (new_slno, name, phone, email)
    cur.execute(insert_query, values)
    con.commit()
    print("✅ Profile created successfully!")

    print('⏳ Loading...')

    # Send registration confirmation email
    from create_profile.mail_on_register import send_registration_mail
    send_registration_mail(email, name, new_slno)

    print("📧 Registration confirmation sent to your email address!")

