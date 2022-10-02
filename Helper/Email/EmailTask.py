from Task.Task import Task,TaskMessage
import smtplib
from email.mime.text import MIMEText
from email.header import  Header


'''
SMTP
(mail_host,mail_user,mail_pass)
'''
class EmailTask(Task):
    def __init__(self,mail_host,mail_user,mail_pass,enconding='utf-8'):
        self.mail_host = mail_host
        self.mail_user = mail_user
        self.mail_pass = mail_pass
        self.enconding = enconding

    def run(self,message:TaskMessage) ->TaskMessage:
        smtpMessage = message.getData('smtp')

        From = smtpMessage.get('from')
        To = smtpMessage.get('to')
        content = smtpMessage.get('content')
        title = smtpMessage.get('title')
        sender = smtpMessage.get('sender')
        receivers = smtpMessage.get('receivers')



        with smtplib.SMTP_SSL(host=self.mail_host,port=465) as smtpobj:
            email_content = MIMEText(content,'plain',self.enconding)
            email_content['From'] = Header(From,self.enconding)
            email_content['To'] = Header(To,self.enconding)
            email_content['Subject'] = Header(title,self.enconding)
            print(receivers)
            smtpobj.login(self.mail_user,self.mail_pass)
            smtpobj.sendmail(sender,receivers,email_content.as_string())

