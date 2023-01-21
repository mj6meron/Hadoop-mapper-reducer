import sys

current_day = None
current_sender = None
count = 0

for line in sys.stdin:
    line = line.strip()
    day, sender, reciever = line.split('\t')
    if current_day == None:
        current_day = day
        count += 1
        continue
    if current_day == day:
        count += 1
    else:
        print(current_day,count)
        current_day = day
        count = 1

if current_day == day:
    print(current_day, count)
