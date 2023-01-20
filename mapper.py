#!/usr/bin/env python
import sys
import pandas as pd

# function to extract the last "clean" message from the email body
def clean_email(email):
    return ''.join([s.strip() for s in email.splitlines()][15:])

# counter variable
counter = 0

# input comes from standard input
for line in sys.stdin:
    # parse the email message
    emailsdf = pd.read_csv(line.strip())
    emailsdf['email_body'] = emailsdf['message'].apply(clean_email)
    # get the subject and body of the email
    emailsdf['index'] = emailsdf.index
    index = emailsdf.get('index')
    body = emailsdf.get('email_body')

    # check if the body is not None
    if body is not None:
        # increase counters
        print('%s\t%s' % (index, body))
        counter += 1
    if counter == 10:
        break
