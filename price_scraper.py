import smtplib

sender = 'katec125@gmail.com'
receivers = ['katec125@gmail.com']

message = """
Here is where the sample text would be
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)
   print("Successfully sent email")

except SMTPException:
   print("Error: unable to send email")
