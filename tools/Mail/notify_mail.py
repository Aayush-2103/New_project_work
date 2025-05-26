def notification_mail(task_name, date_time, note, name, receiver):
    #this to send the notification mail to the user
    import smtplib
    from email.message import EmailMessage
    
    sender_mail = 'aayushtalukdar@gmail.com'
    password = 'jage ssmf vnig ccib'

    msg = EmailMessage()

    message = f'''
Hello {name}

This is a gentle reminder for your upcoming task: {task_name}.

🗓 Scheduled Date & Time: {date_time}
📝 Note: {note} 

We hope this reminder helps you stay on track. Feel free to reach out if you need any assistance managing your tasks.

Thank you
Best regards,
Your To-Do App Team
'''
    
    msg.set_content(message)
    msg['Subject'] = f'⏰ Reminder: Upcoming Task - {task_name}'
    msg['From'] = sender_mail
    msg['To'] = receiver

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_mail, password)
        smtp.send_message(msg)