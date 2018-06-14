import mysql.connector
import imaplib
import email

cnx= mysql.connector.connect(host="127.0.0.1", user="root",
passwd="snl231096", db="challenge_3")

cursor = cnx.cursor()

user = 'sofianlucena@gmail.com'
pwd = 'snl231096!'

#def get_body(msg):
    #if msg.is_multipart():
        #return get_body(msg.get_payload(0))
    #else:
        #return msg.get_payload(None, True)



server = imaplib.IMAP4_SSL("imap.gmail.com")
server.login (user, pwd)
sts, count = server.select('INBOX')

rslt, dat =server.uid('search', None, "ALL")
inbox_item_list = dat[0].split()
"""for num in dat[0].split():

    data = server.fetch('(BODY[HEADER.FIELDS (SUBJECT)])')
   # print(data)
   # if 'DevOps' in data is True:
    #    print ('something')
    #else:
     #   print('nothing')

#email_uid = dat[0].split()
#status, dat = server.fetch(count[0],'(UID BODY[TEXT])')
#raw_email = dat[0][1]
#s = str(raw_email)
#email_message = email.message_from_string(s)
"""

def get_first_text_block(self, email_message):
    maintype = email_message.get_content_maintype()

    if maintype == 'multipart':
        for part in email_message.get_payload():
            if part.get_content_maintype() == 'text':
                return part.get_payload()
    elif maintype == 'text':
        return email_message.get_payload()
caca= get_first_text_block()
print (caca)



#for i in inbox_item_list:
    #result, data = server.fetch(i, '(RFC822)')
    #i.decode('ASCII')
    #raw = email.message_from_bytes(data[0][1])
    #print(get_body(raw))

    #print(data)
    #print (b"DevOps" in body)
