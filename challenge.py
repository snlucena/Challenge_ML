import mysql.connector
import imaplib
import email

cnx= mysql.connector.connect(host="127.0.0.1", user="root",
passwd="snl231096", db="challenge_3")

cursor = cnx.cursor()

user = 'sofianlucena@gmail.com'
pwd = 'snl231096!'

def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)

def search(key, value, server) :
    result, data = server.search(None, key, '"()"'.format(value))
    return data

def get_emails(result_bytes):
    msgs = []
    for num in result_bytes[0].split() :
        typ, data = server.fetch(num, '(RFC822)')
        msgs.append(data)
    return msgs

server = imaplib.IMAP4_SSL("imap.gmail.com")
server.login (user, pwd)
server.select('INBOX')

rslt, dat =server.uid('search', None, "ALL")
inbox_item_list = dat[0].split()

for i in inbox_item_list:
    result, data = server.fetch(i, '(RFC822)')
    raw = email.message_from_bytes(data[0][1])
    body = (get_body(raw))

msgs = get_emails(search('SUBJECT', 'DevOps', server))

print(msgs)

#result, data = server.fetch(b'7', '(RFC822)')
#raw = email.message_from_bytes(data[0][1])

#print(inbox_item_list)
#print(get_body(raw))

#s = server.select('INBOX')
#result, data = server.uid('search', None, "ALL")
#inbox_item_list = data[0].split()
#first_email_id = int(inbox_item_list[0])
#latest_email_id = int(inbox_item_list[-1])

#for i in range(latest_email_id,first_email_id, -1):
           # typ, dat = server.fetch(i, '(RFC822)' )
#headers = Parser(policy=default).parsestr(inbox_item_list)
