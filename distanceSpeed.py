# Finding speed by distance in meters and time in seconds and speed in kmph

distance = int(input())
time = int(input())

if time <= 0 or time >60:
    print("error")
else:
    speed = (distance / time ) * 18/5
    print(speed)