

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

    # Convert the row to a DataFrame
    row_df = pd.DataFrame([row], index=[0])

    # Concatenate the row DataFrame with the existing DataFrame
    cleanedDF = pd.concat([cleanedDF, row_df], ignore_index=True)

cleanedDF.dropna()
ln2 = emailsdf.shape[0]
for i in range(0, ln2):
    print(cleanedDF.loc[i]['Date'])
    # print('%s\t%s\t%s' % (cleanedDF.loc[i]['Date'], cleanedDF.loc[i]['Sender'], cleanedDF.loc[i]['Receiver']))
    # print("sender -> ", sender)
    # print("reciever -> ", reciever)
    # print("content -> ", content)
