def stoh(seconds):
    hours=seconds//3600
    minutes=(seconds%3600)//60
    seconds=seconds%60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

seconds=int(input("Enter the time in seconds: "))
actual_time=stoh(seconds)
print("Time in HH:MM:SS format",actual_time)