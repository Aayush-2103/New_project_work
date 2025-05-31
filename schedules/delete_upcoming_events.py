import datetime



# Feature to delete user's upcoming/future events
def delete_events(events, uid):

    now = datetime.datetime.now()
    # Fetching only upcoming events for this user
    upcoming_events = []
    for event in events:
        if event['user_id'] == uid and event['datetime'] > now:
            upcoming_events.append(event)

    if not upcoming_events:
        print("No upcoming events to delete.")
        return events




    print("Your upcoming events:")
    for i in range(len(upcoming_events)):
        event = upcoming_events[i]
        print(str(i+1) + ". " + event['task'] + " at " + str(event['datetime']) + " (ID: " + str(event['id']) + ")")

    try:
        num = int(input("Enter the number of the event to delete (0 to cancel): "))
    except:
        print("Invalid input.")
        return events

    if num == 0:
        print("Cancelled.")
        return events

    if 1 <= num <= len(upcoming_events):
        del_id = upcoming_events[num-1]['id']
        new_events = []
        for event in events:
            if event['id'] != del_id:
                new_events.append(event)
        print("Event deleted.")
        return new_events
    else:
        print("Invalid choice.")
        return events
