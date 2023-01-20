#!/usr/bin/env python

import sys
import email

# input comes from standard input
for line in sys.stdin:
    # parse the email message
    msg = email.message_from_string(line)

    # get the subject and body of the email
    subject = msg.get('subject')
    body = msg.get_payload()

    # increase counters
    print('%s\t%s' % (subject, body))
