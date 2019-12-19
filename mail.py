import sys
import urllib.request as urllib2
import smtplib
import time
def is_connected():
    try:
        urllib2.urlopen('http://216.58.192.142',timeout=1)
        return True
    except urllib2.URLError as err:
        return False
    
def MailSender(user,password):
    sent_from=user
    to=['vaibhavgopanpalli18@gmail.com']
    SUBJECT= "First Pdf through automail"
    TEXT="Love YOu Vk....."
    Att=open("Marvellous Angular - New Features added in Angular 8.pdf","rb")
    message = 'Subject: {}\n\n{}\n\n{}'.format(SUBJECT, TEXT,Att)

    try:
        server=smtplib.SMTP_SSL('smtp.gmail.com',465)
        print(server)
        ms=server.ehlo()
        print(ms)
        rs=server.login(user,password)
        print(rs)
        d=server.sendmail(sent_from,to,message)
        print(d)
        server.close()

        print("Mail sent successfully...")
    except Exception as E:
        print(E)
        print("Unable to Send..")
def main():
    print("_____________vAiBhAv______________")
    print(sys.argv[0])
    user='mahadevgopanpalli@gmail.com'
    password='Vaibhav18vk'
    connected=is_connected()
    print(connected)
    if connected:
        MailSender(user,password)
    else:
        print("Unsuccessful..")


if __name__ == "__main__":
    main()