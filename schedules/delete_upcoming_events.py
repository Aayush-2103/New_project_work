import datetime



# Feature to delete user's upcoming/future events
def delete_events(cur, uid):


    now = datetime.datetime.now()
    # Fetch upcoming events for this user
    query = "SELECT SLNO, TASK_NAME, DATE_AND_TIME, NOTE FROM events WHERE SLNO = %s AND DATE_AND_TIME > %s"
    cur.execute(query, (uid, now))
    upcoming_events = cur.fetchall()

    if not upcoming_events:
        print("No upcoming events to delete.")
        return

    print("Your upcoming events:")
    i = 0
    while i < len(upcoming_events):
        event = upcoming_events[i]
        print(str(i+1) + ". " + event[1] + " at " + str(event[2]) + " (Event ID: " + str(event[0]) + ")")
        i += 1

    try:
        num = int(input("Enter the number of the event to delete (0 to cancel): "))
    except:
        print("Invalid input! Please enter a number.")
        return

    if num == 0:
        print("Deletion Cancelled!")
        return

    if 1 <= num <= len(upcoming_events):
        del_slno = upcoming_events[num-1][0]
        del_date = upcoming_events[num-1][2]
        del_query = "DELETE FROM events WHERE SLNO = %s AND DATE_AND_TIME = %s"
        cur.execute(del_query, (del_slno, del_date))
        print("Event deleted successfully!")
    else:
        print("Invalid choice! Please enter a valid number.")
        return
