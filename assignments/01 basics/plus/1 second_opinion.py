total_seconds_str = input("Input seconds: ")
total_seconds_int = int(total_seconds_str)

hours = total_seconds_int // 3600
remainder = total_seconds_int % 3600
minutes = remainder // 60
seconds = remainder % 60

# Alternatively:
# seconds = total_seconds_int % 60
# total_minutes = total_seconds_int // 60
# minutes = total_minutes % 60
# hours = total_minutes // 60

print(hours, ":", minutes, ":", seconds)
