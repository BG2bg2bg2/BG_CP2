from datetime import datetime

def get_clean_time():
    #return current time formatted as MM-DD-YYYY HH:MM:SS (24-hour)
    now = datetime.now()
    return now.strftime("%m-%d-%Y %H:%M:%S")