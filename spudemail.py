from __future__ import unicode_literals

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
import email
from log import logit

from imapclient import IMAPClient
import os.path
from os.path import split as psplit

# username = "spudwalks@gmail.com"
username = "spudwalks@comcast.net"

def sendMail(recipient, subject, message=None, picture=None, file=None, series=None, seriesRange=None):
    """this is some test documentation in the function"""

    #SECRET = getSecret() # gmail version
    SECRET = "1!{0}".format(getSecret()[:13])

    password = SECRET

    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = recipient
    msg['Subject'] = subject
    
    if message:
        msg.attach(MIMEText(message))

    if picture:
        msgImage = getMailPicture(picture)
        # Define the image's ID as referenced above
        if msgImage:
            msgImage.add_header('Content-ID', 'pic')
            msgImage.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(psplit(picture)[-1]))
            msg.attach(msgImage)

    if series and seriesRange:
        for i in seriesRange:
            picname = series.format(i)
            msgImage = getMailPicture(picname)
            # Define the image's ID as referenced above
            if msgImage:
                msgImage.add_header('Content-ID', 'pic')
                msgImage.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(psplit(picname)[-1]))
                msg.attach(msgImage)
        
    if file:
        try:
            with open(file, 'r') as theFile:
                msgLog=theFile.read()  
            msg.attach(MIMEText(msgLog))
        except Exception as e:
            logit(str(e))

    try:
        logit('sending mail to ' + recipient + ' re: ' + subject)

        # mailServer = smtplib.SMTP('smtp.gmail.com', 587)
        mailServer = smtplib.SMTP('smtp.comcast.net', 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(username, password)
        mailServer.sendmail(username, recipient, msg.as_string())
        mailServer.close()

    except Exception as e:
        logit(str(e))
 
def getMailPicture(filename):
    msgImage=None
    if os.path.exists(filename):
        fp = open(filename, 'rb')
        msgImage = MIMEImage(fp.read(),_subtype='jpg')
        fp.close()

    return msgImage

def getMail():

    # SECRET = getSecret()
    SECRET = "1!{0}".format(getSecret()[:13])


    # server = IMAPClient("imap.gmail.com", use_uid=True, ssl=True)
    server = IMAPClient("imap.comcast.net", use_uid=True, ssl=True)
    server.login(username, SECRET)

    select_info = server.select_folder('INBOX')
#     print('%d messages in INBOX' % select_info['EXISTS'])
# 
    messages = server.search(['NOT', 'DELETED'])
#     print("%d messages that aren't deleted" % len(messages))

    theMsgs = []
    response = server.fetch(messages, ['RFC822'])
    for messagegId,data in response.iteritems():
            messageString = data['RFC822']
            msgStringParsed = email.message_from_string(messageString)
            messageFrom = msgStringParsed['From']
            messageSubj = msgStringParsed['Subject']
            
            bodytext=''
            for part in msgStringParsed.walk():
                if part.get_content_type() == "text/plain":
                    bodytext=part.get_payload().strip()

            theMsgs.append({'from':messageFrom, 'subj':messageSubj.strip(), 'body':bodytext})

    server.delete_messages(response.keys())

    server.logout()
    return theMsgs

def getSecret():
    f = None
    try:
        f = open('secret.txt')
    except:
        pass

    if f is None:
        try:
            f = open('/home/pi/spudcam/secret.txt')
        except:
            pass

    if f is not None:
        line = f.readline().strip()
        f.close()
        return line
    else:
        logit('no secret file!')
        return ''


def main():
    """ test the email connection """
    sendMail('aoppenheimer@gmail.com','Email Test',"woo!")


if __name__ == "__main__":
    main()    