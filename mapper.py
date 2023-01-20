"""
Mapper.py code written by Meron
"""

import sys
import pandas as pd
import email

# function to extract the last "clean" message from the email body
def clean_email(email):
    return ''.join([s.strip() for s in email.splitlines()][15:])

# counter variable
counter = 0

emailsdf = pd.read_csv(sys.stdin, nrows=10)
ln = emailsdf.shape[0]
for i in range(0, ln):
    message = emailsdf.loc[i]['message']
    e = email.message_from_string(message)
    sender = e.get('From')
    reciever = e.get('To')

    """
    We can also map out and manipulate the content, But for this case, 
    only a pair of a sender and reciever is needed
    """
    content = e.get_payload()  
    # Here we cound use and map out the content
    #print('%s\t%s\t%s' % (sender, reciever, content))

    print('%s\t%s' % (sender, reciever))

    #print("sender -> ", sender)
    #print("reciever -> ", reciever)
    #print("content -> ", content)

