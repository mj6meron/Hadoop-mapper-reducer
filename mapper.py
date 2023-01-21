"""
Mapper.py code written by Meron
"""

import sys
import pandas as pd
import email

emailsdf = pd.read_csv(sys.stdin, nrows=10)
ln = emailsdf.shape[0]


cleanedDF = pd.DataFrame()
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
    datearray = e.get('Date').split()[1:4]
    date = '%s,%s,%s' % (datearray[1], datearray[0], datearray[2])

    row = {"Date": date, "Sender": sender, "Receiver": reciever}
    temp_df = pd.DataFrame([row])
    cleanedDF = cleanedDF.append(temp_df, ignore_index=True)

    print('%s\t%s\t%s' % (date, sender, reciever))

cleanedDF.dropna()
ln2 = emailsdf.shape[0]
for i in range(0, ln2):
    print('%s\t%s\t%s' % (cleanedDF.loc[i]['Date'], cleanedDF.loc[i]['Sender'], cleanedDF.loc[i]['Receiver']))



    #print("sender -> ", sender)
    #print("reciever -> ", reciever)
    #print("content -> ", content)
