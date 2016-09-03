from __future__ import unicode_literals

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
import email

from imapclient import IMAPClient


def sendMail(recipient, subject, message):
    """this is some test documentation in the function"""

    SECRET = getSecret()

    username = "spudwalks@gmail.com"
    password = SECRET

    msg = MIMEMultipart()
    msg['From'] = "spudwalks@gmail.com"
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(message))


    fp = open('pic.jpg', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', 'pic')
    msg.attach(msgImage)

    try:
        print('sending mail to ' + recipient + ' on ' + subject)

        mailServer = smtplib.SMTP('smtp.gmail.com', 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(username, password)
        mailServer.sendmail(username, recipient, msg.as_string())
        mailServer.close()

    except Exception as e:
        print(str(e))
 

def getMail():

    SECRET = getSecret()


    server = IMAPClient("imap.gmail.com", use_uid=True, ssl=True)
    server.login("spudwalks@gmail.com", SECRET)

    select_info = server.select_folder('INBOX')
    print('%d messages in INBOX' % select_info['EXISTS'])

    messages = server.search(['NOT', 'DELETED'])
    print("%d messages that aren't deleted" % len(messages))

    print("Messages:")
    theMsgs = []
    response = server.fetch(messages, ['RFC822'])
    for messagegId,data in response.iteritems():
            messageString = data['RFC822']
            msgStringParsed = email.message_from_string(messageString)
            messageFrom = msgStringParsed['From']
            messageSubj = msgStringParsed['Subject']
            theMsgs.append({'from':messageFrom, 'subj':messageSubj})
            print 'From:{0}\nSubject:{1}'.format(messageFrom, messageSubj)
                                                
    print('keys: {0}'.format(response.keys()))

    server.logout()
    return theMsgs

def getSecret():
    f = open('secret.txt')
    line = f.readline().strip()
    return line