import os
import sys
import imaplib

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.dirname(BASE_DIR))

from passconfig import PassConfig


# pc = PassConfig(section='imap4')
pc = PassConfig(section='imap4', username='suqingdong@novogene.com', password='wrong-pass')
username, password = pc.get()  # input username and password at the first time
print(username, password)

host = 'smtp.exmail.qq.com'
mail = imaplib.IMAP4_SSL(host)

try:
    res = mail.login(username, password)
except imaplib.IMAP4.error as e:
    print(e)
    exit()

print(res)
if res[0] == 'OK':
    pc.save()
else:
    exit(1)

for each in mail.list()[1]:
    catalog = str(each).split(' "/" ')[1].replace('&', '+').encode().decode('utf-7')
    print(catalog)
