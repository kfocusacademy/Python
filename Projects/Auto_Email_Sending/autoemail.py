from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import schedule
import time
import os

# Function to create the message to be sent 
def message(subject,text):  
    msg = MIMEMultipart()
    msg.attach(MIMEText(text))
    msg['Subject'] = subject
    return msg

# Function to establish email connection, send the message to given recipients 
def mail():
    # Initiate email connection 
    smtp = smtplib.SMTP ('smtp.gmail.com',587)
    smtp.ehlo() # to send EHLO command 
    smtp.starttls() # to enable transfort layer security 
    smtp.login('kfocusacademy@gmail.com','pijzgsvptdxrurwe')
    print("Email connection established")
    # Call the message function 
    msg = message("Sev1 defect logged","This email is to inform all of you about a SEv1 ticket logged in production, the service desk team is looking into it")
    # Send the email to the recipients 
    to = ["ravis.buddha@gmail.com"]
    smtp.sendmail(from_addr="kfocusacademy@gmail.com", to_addrs=to, msg=msg.as_string())
    print("Email sent successfully")
    smtp.quit()

schedule.every(2).seconds.do(mail)

while True:
    schedule.run_pending()
    time.sleep(1)




