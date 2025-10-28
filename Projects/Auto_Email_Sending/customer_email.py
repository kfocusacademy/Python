# Program to load customer data from a xls file and send personalized emails with attachments
import pandas as pd
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication  
from email.mime.multipart import MIMEMultipart
import smtplib 
import os
import schedule
import time

# Function to create the message to be sent
def message(subject, text, img_path, attachment_path, to):  
    msg = MIMEMultipart()
    msg.attach(MIMEText(text))
    msg['Subject'] = subject
    msg['To'] = to

    # Attach image
    with open(img_path, 'rb') as img:
        img_data = img.read()
    image = MIMEImage(img_data, name=os.path.basename(img_path))
    msg.attach(image)

    # Attach file
    with open(attachment_path, 'rb') as attachment:
        attach_data = attachment.read()
    attachment = MIMEApplication(attach_data, name=os.path.basename(attachment_path))
    attachment['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment_path)}"'
    msg.attach(attachment)

    return msg

# Function to establish email connection, send the message to given recipients
def mail():
    print("before email connection established ")
    # Initiate email connection 
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()  # to send EHLO command 
    smtp.starttls()  # to enable transport layer security 
    smtp.login('kfocusacademy@gmail.com','pijzgsvptdxrurwe')
    print("Email connection established")
    # Load customer data from xls
    df = pd.read_excel(r'C:\Ravi\Python\Projects\Auto_Email_Sending\customer_details.xlsx')
    for index, row in df.iterrows():
        print(row['email'], row['customer_name'],row['email_sent'])
        if row['email_sent'] == 'Yes':
            print(f"Email already sent to {row['email']}, skipping...")
            continue    
        to = row['email']
        name = row['customer_name']
        subject = "Personalized Offer Just for You!"
        text = f"Dear {name},\n\nWe are excited to offer you a special discount on our products. Please find the details in the attached document.\n\nBest regards,\nYour Company"
        img_path = r'C:\Ravi\Python\Projects\Auto_Email_Sending\kfocus_offer.jpg'  # Path to the image to be attached
        attachment_path = r'C:\Ravi\Python\Projects\Auto_Email_Sending\kfocus_offer.pdf'  # Path to the PDF to be attached
        msg = message(subject, text, img_path, attachment_path, to)
        smtp.sendmail(from_addr='kfocusacademy@gmail.com', to_addrs=to, msg=msg.as_string())
        print(f"Email sent successfully to {to}")
        # update excel file to mark email as sent
        df.at[index, 'email_sent'] = 'Yes'
    df.to_excel(r'C:\Ravi\Python\Projects\Auto_Email_Sending\customer_details.xlsx', index=False)
    # Close the SMTP server connection
    smtp.quit()
    
# Calling the mail function to send the email
mail()

# In case you want to schedule the email sending at regular intervals, uncomment the below lines
#schedule.every(2).seconds.do(mail)

#while True:
#    schedule.run_pending()
#    time.sleep(1)