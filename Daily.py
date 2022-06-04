import smtplib
import time
import schedule
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def auto_mail():
   mail_content = '''type your mail context. '''
   sender_address = 'yourMail@gmail.com'
   sender_pass = 'YourPassMail'
   receiver_address = 'SenderMail@gmail.com'
   message = MIMEMultipart()
   message['From'] = sender_address
   message['To'] = receiver_address
   message['Subject'] = 'The sub in the mail'

   message.attach(MIMEText(mail_content, 'plain'))
   session = smtplib.SMTP('smtp.gmail.com', 587)
   session.starttls()
   session.login(sender_address, sender_pass)
   text = message.as_string()
   session.sendmail(sender_address, receiver_address, text)

   session.quit()
   print('Mail Sent')

schedule.every().day.at('10:00').do(auto_mail)
schedule.every().day.at('10:32').do(auto_mail)
while 1:
   schedule.run_pending()
   time.sleep(1)
