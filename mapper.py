#!/usr/bin/env python

import sys
import email

# counter to keep track of the number of processed lines
counter = 0

# input comes from standard input
for line in sys.stdin:

    # check if the counter is less than or equal to 10
    if counter <= 10:
        # parse the email message
        msg = email.message_from_string(line)

        # get the subject and body of the email
        subject = msg.get('subject')
        body = msg.get_payload()

        # check if the subject is not None
        if (subject and body) is not None:
            # increase counters
            print('%s\t%s' % (subject, body))

            # increment the counter
            counter += 1
    else:
        # exit the loop if the counter is greater than 10
        break
