from datetime import datetime

def get_clean_time():
    #retun current time formatted as MM/DD/YYYY HH:MM:AM/PM
    now = datetime.now
    return now.strftime("%m/%d/%Y %I:%M %p")