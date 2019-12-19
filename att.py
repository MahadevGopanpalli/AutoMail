from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
from email.mime.base import MIMEBase

import sys
import urllib.request as urllib2
import smtplib
import time
def is_connected():
    try:
        
        urllib2.urlopen('http://facebook.com',timeout=1)
        return True
    except urllib2.URLError as err:
        return False
    
def MailSender(user,password):
    sent_from=user
    to='ekkaldevi143@gmail.com'
    body="Love you King Kohli...."
    message = MIMEMultipart("alternative")
    message["Subject"] = "First automated mail with attatchment"
    message["From"] = user
    message["To"] = to
    message.attach(MIMEText(body, "plain"))

    filename = "Marvellous Angular - New Features added in Angular 8.pdf" 


    with open(filename, "rb") as attachment:
    
    
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    
    encoders.encode_base64(part)


    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )


    message.attach(part)
    message.attach(part)
    text = message.as_string()

    try:
        server=smtplib.SMTP_SSL('smtp.gmail.com',465)
        print(server)
        ms=server.ehlo()
        print(ms)
        rs=server.login(user,password)
        print(rs)
        d=server.sendmail(sent_from,to,text)
        print(d)
        server.close()

        print("Mail sent successfully...")
    except Exceptionbalaji1 as E:
        print(E)
        print("Unable to Send..")
def main():
    print("_____________vAiBhAv______________")
    print(sys.argv[0])
    user='mahadevgopanpalli@gmail.com'
    password='---------'
    connected=is_connected()
    print(connected)
    if connected:
        MailSender(user,password)
    else:
        print("Unsuccessful..")


if __name__ == "__main__":
    main()
