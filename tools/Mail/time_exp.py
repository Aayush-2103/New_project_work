#setting the expiry time

def exp_time():
    from datetime import datetime, timedelta
    import pytz

    #getting the correct time zone
    tz = pytz.timezone('Asia/Kolkata')    
    now = datetime.now(tz)

    #adding extra 10 minutes
    expiry_time = now + timedelta(minutes=10)

    #formatting it in 24hr format
    time = expiry_time.strftime('%H:%M; %d %B, %Y')

    return time