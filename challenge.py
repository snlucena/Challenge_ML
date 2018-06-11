import mysql.connector
import imaplib
import email

cnx= mysql.connector.connect(host="127.0.0.1", user="root",
passwd="**********", db="challenge_3")

cursor = cnx.cursor()

user = 'usuario@gmail.com'
pwd = 'contraseña'

def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)



server = imaplib.IMAP4_SSL("imap.gmail.com")
server.login (user, pwd)
server.select('INBOX')

rslt, dat =server.uid('search', None, "ALL")
inbox_item_list = dat[0].split()

for i in inbox_item_list:
    result, data = server.fetch(i, '(RFC822)')
    raw = email.message_from_bytes(data[0][1])
    body = (get_body(raw))
    print(body)