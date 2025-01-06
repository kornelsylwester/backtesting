from datetime import datetime

start_time = "2024-08-02T00:00:00"

def convert_human_readable_to_unix(*args):
    time_format = "%Y-%m-%dT%H:%M:%S"
    unix_timestamps = [int(datetime.strptime(arg, time_format).timestamp()) for arg in args]
    return unix_timestamps

def convert_unix_to_human_readable(*args):
    # Convert the Unix timestamp to a datetime object
    readable_datetimes = [datetime.fromtimestamp(arg).strftime("%Y-%m-%dT%H:%M:%S") for arg in args]
    # Format the datetime object to a readable string
    #readable_date = dt_object.strftime("%Y-%m-%d %H:%M")
    return readable_datetimes

# print(convert_unix_to_human_readable(1733029140, 1732985940, 1782985940))
# print(convert_human_readable_to_unix("11-30-2024 22:59:00","12-30-2024 22:59:00","11-14-2024 23:59:00"))

