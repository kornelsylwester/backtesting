from unix_time_converter import convert_human_readable_to_unix

increment = 300#1 = 1 minute
exchange_fee = 0.006
stop_loss_percentage = 0.99
start_time = "2024-08-15T12:00:00"  # "%Y-%m-%dT%H:%M:%S" format
end_time = "2024-12-30T12:00:00"


start_time_timestamp = int(convert_human_readable_to_unix(start_time)[0])
end_time_timestamp = int(convert_human_readable_to_unix(end_time)[0])