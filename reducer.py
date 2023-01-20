#!/usr/bin/env python

import sys

current_subject = None
current_body = None

subject = None

# input comes from standard input
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into fields
    subject, body = line.split('\t')

    if current_subject == subject:
        current_body += body
    else:
        if current_subject:
            # write result to standard output
            print ('%s\t%s' % (current_subject, current_body))
        current_body = body
        current_subject = subject

# do not forget to output the last subject if needed!
if current_subject == current_subject:
    print ('%s\t%s' % (current_subject, current_body))
