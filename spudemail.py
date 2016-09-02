import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

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
 
    
def getSecret():
    f = open('secret.txt')
    line = f.readline().strip()
    return line