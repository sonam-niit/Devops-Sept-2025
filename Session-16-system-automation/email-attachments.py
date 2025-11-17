# Sending Emails with attachments
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

def send_email(subject,body):
    sender_email="your email id"
    receiver_email="receivers_email_id"
    password=os.environ.get("EMAIL_PASSWORD") # fetch from env variable
    
    # Export variable from Linux: export EMAIL_PASSWORD="your_password"
    msg=MIMEMultipart()
    msg['subject']=subject
    msg["from"]=sender_email
    msg["to"]=receiver_email
    
    # Add message
    msg.attach(MIMEText("<h1>"+body+"</h1>",'html')) # Add text message
    filename="app.log"
    
    with open(filename,'rb') as attachment:
        mime_base=MIMEBase("application","octet-stream")
        mime_base.set_payload(attachment.read())
    
    # Encode file in ASCII for Email
    encoders.encode_base64(mime_base) 
    mime_base.add_header('content-disposition', f'attachment', filename='bank-statement.log') 
    msg.attach(mime_base)
    
    with smtplib.SMTP("smtp.gmail.com","587") as server:
        server.starttls() #encrypt connection
        server.login(sender_email,password)
        server.send_message(msg)
        print("Message Send Successfully")
    
send_email("Alert Message","Bank Statement for Month of October 2025")

