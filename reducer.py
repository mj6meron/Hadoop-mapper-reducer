import sys

current_day = None
current_sender = None
count = 0

for line in sys.stdin:
    line = line.strip()
    day, sender, reciever = line.split('\t')
    if current_day == day:
        count += 1
    else:
        if current_day:
            print(current_day,count)
        current_day = day
        count = 1

if current_day == day and current_sender == sender:
    print(current_day,current_sender,count)
