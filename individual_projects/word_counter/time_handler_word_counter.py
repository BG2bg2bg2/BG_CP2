from datetime import datetime

def get_clean_time():
    # return current time formatted as YYYY-MM-DD HH:MM:SS (24-hour)
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")