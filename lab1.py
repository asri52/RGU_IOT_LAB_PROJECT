import datetime
name = input("Enter your name:")

dt = datetime.datetime.now()
hours = dt.hour

if 0<hours>11:
    print("Good Morning",name)
elif 12<hours>17:
    print("Good afternoon",name)
else:
    print("Good evening",name)
