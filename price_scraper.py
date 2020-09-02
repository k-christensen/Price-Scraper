import smtplib

from smtplib import SMTPException

from ps_personal_keys import password
from ps_personal_keys import email

sender = email
receivers = [email]

message = """
From: From Person <katec125@gmail.com>
To: To Person <katec125@gmail.com>
Subject: SMTP e-mail test
Here is where the sample text would be
"""
try:
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.ehlo()
    session.starttls()
    session.ehlo()
    session.login(sender, password)
    session.sendmail(sender, receivers, message)
    session.quit()
except SMTPException:
    print('Error')
