#!/usr/bin/env python
import sys
import pandas as pd

# function to extract the last "clean" message from the email body
def clean_email(email):
    return ''.join([s.strip() for s in email.splitlines()][15:])

# counter variable
counter = 0

emailsdf = pd.read_csv(sys.stdin, nrows=10)
emailsdf['email_body'] = emailsdf['message'].apply(clean_email)

for index, row in emailsdf.iterrows():
    if row["email_body"] is not None:
        #print('%s\t%s' % (index, row["email_body"]))
        counter += 1
        print('%s\t%s' % (counter, row["email_body"]))

