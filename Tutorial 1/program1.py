def seconds_to_hhmmss(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

time_in_seconds = int(input("Enter time in seconds: "))
print(seconds_to_hhmmss(time_in_seconds))
