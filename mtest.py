#! / Usr / bin / python

#Sends all files via mail
#Example usage: python sendMail.py file1.txt, file2.txt ...

import sys , smtplib , os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
# from email.Utils import Format
from email import encoders

class SendMail ( object ) :
    mailadress =  'mpcaproj123@gmail.com'
    smtpserver =  'smtp.googlemail.com'
    username =  'mpcaproj123'
    password =  'raspberrypi'

    def send ( self , files ) :
        # Gather information, prepare mail
        to = self.mailadress
        From = self.mailadress
         #Subject contains previews of filenames

        subject =  'INTRUDER ALERT'
        msg = self.prepareMail ( From , to , subject , files )

        #Connect to server and send mail
        server = smtplib.SMTP ( self.smtpserver )
        server.ehlo ( )  #Has something to do with sending information
        server.starttls ( )  # Use encrypted SSL mode
        server.ehlo ( )  # To make starttls work
        server.login ( self.username , self.password )
        failed =server.sendmail ( From , to , msg.as_string ( ) )
        server.quit ( )

    def prepareMail ( self , From , to , subject , attachments ) :
        msg = MIMEMultipart ( )
        msg [ 'From' ]  = From
        msg [ 'To' ]  = to
        # msg [ 'Date' ]  = formatdate ( localtime = True )
        msg [ 'Subject' ]  = subject

        # The Body message is empty
        msg.attach ( MIMEText ( "" )  )

        for  file  in attachments :
          #We could check for mimetypes here, but I'm too lazy
            part = MIMEBase ( 'application' ,  'octet-stream' )
            part.set_payload (  open ( file , "rb" ).read ( )  )
            encoders.encode_base64 ( part )
            part.add_header ( 'Content-Disposition' ,  'attachment; filename = "% s"'  % os.path.basename ( file ) )
            msg.attach ( part )
          #Delete created Tar
        return msg

def mailit() :
    mail = SendMail ( )
    # Send all files included in command line arguments
    list = ['test-data/test1.jpg','test-data/test2.jpg','test-data/test3.jpg','test-data/test4.jpg','test-data/test5.jpg']
    mail.send (list)
    for file in list:
        os.remove(file)
# The following code might have to be commented on:

# server = smtplib.SMTP ( self.Smtpserver )
#     server.ehlo ( )  #Has something to do with sending information
#     server.starttls ( )  # Use encrypted SSL mode
#     server.ehlo ( )  # To make starttls work
#     server.login ( self.username , self.password )
