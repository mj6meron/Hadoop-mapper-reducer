#!/usr/bin/env python

import sys

current_date = None
current_count = 0
date = None

# initialize count dictionary
count = {}

# input comes from standard input
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    date, sender, reciever = line.split('\t', 2)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_date == date:
        current_count += count
    else:
        if current_date:
            # write result to standard output
            print ('%s\t%s' % (current_date, current_count))
        current_count = count
        current_date = date

# do not forget to output the last word if needed!
if current_date == date:
    print ('%s\t%s' % (current_date, current_count))
