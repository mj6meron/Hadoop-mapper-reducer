"""
This works on sorted input. The input has to be sorted.
"""

import sys

current_day = None
current_sender = None
count = 0

for line in sys.stdin:
    day = line.strip()
    if current_day == day:
        count += 1
    else:
        if current_day:
            print('%s\t%s' % (current_day, count))
        current_day = day
        count = 1


"""
The if statement at the end of the file is checking if the current day is the same as the last day that was processed. 
"""

if current_day == day:
    print('%s\t%s' % (current_day, count))
