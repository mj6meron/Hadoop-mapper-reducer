#!/usr/bin/env python
import sys
import pandas as pd

# function to extract the last "clean" message from the email body
def clean_email(email):
    return ''.join([s.strip() for s in email.splitlines()][15:])

# counter variable
counter = 0

emailsdf = pd.read_csv(sys.stdin)    
emailsdf['email_body'] = emailsdf['message'].apply(clean_email)

# input comes from standard input
for line in emailsdf['email_body']:
    # parse the email message
    
    index = emailsdf.emailsdf.index
    body = line

    # check if the body is not None
    if body is not None:
        # increase counters
        print('%s\t%s' % (index, body))
        counter += 1
    if counter == 10:
        break
