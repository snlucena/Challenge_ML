import mysql.connector
import imaplib


_host_ = input("Ingresar host mysql:")
_user_ = input("Ingresar usuario mysql:")
_password_ = input("Ingresar password mysql:")
_database_ = input("Ingresar database:")
cnx= mysql.connector.connect(host= _host_, user= _user_,
passwd= _password_, db= _database_)

cursor = cnx.cursor()

user = input("Ingresar usuario gmail:")
pwd = input("Ingresar contraseña gmail:")


server = imaplib.IMAP4_SSL("imap.gmail.com") #conexión con servidor gmail
server.login (user, pwd)                     #acceso a la cuenta
sts, count = server.select('INBOX')          #seleccion de INBOX

rslt, data =server.uid('search', None, "ALL") #busca la cantidad de mails en INBOX, devuelve en forma de string: [b' 1 2 3 4 5...] (asumo string porque sino no podria aplicar el .split() en la sig linea
inbox_item_list = data[0].split()          #convierte a data de string a lista de cada una de sus "palabras", en este caso numeros

for i in inbox_item_list:
    typ, subjects = server.fetch(i, '(BODY[HEADER.FIELDS (SUBJECT)])') #fetch de los subject de los emails dentro de inbox_item_list
    print(subjects)                                                    #print de los subject en forma de lista de tuplas(?) pero en bytes

for i in inbox_item_list:
    type, bodies = server.fetch(i, '(UID BODY[TEXT])')                 #fetch de los bodies de los emails dentro de inbox_item_list
    print (bodies)                                                     #print de los bodies en forma de lista de tuplas(?) pero en bytes