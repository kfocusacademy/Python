import smtplib

sender_email = "kfocusacademy@gmail.com"
app_password = "pijzgsvptdxrurwe"
receiver_email = "ravis.buddha@gmail.com"

message = """\
Subject: Test Email

This is a test email from Python."""

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, app_password)
    server.sendmail(sender_email, receiver_email, message)