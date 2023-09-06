import time
times = time.strftime('%H:%M:%S')
print("Current time:", times)
current_hour = int(times[:2])  # Extract the hour portion and convert to integer
if 6 <= current_hour < 12:
    print('Good morning sir !!')
elif 12 <= current_hour < 18:
    print("Good afternoon sir !!")
elif 18 <= current_hour < 23:
    print("Good evening sir !!")
else:
    print("good night sir")

    

