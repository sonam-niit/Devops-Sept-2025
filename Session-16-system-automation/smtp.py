# Sending Text Emails
import smtplib
from email.mime.text import MIMEText

def send_email(subject,body):
    sender_email="your_email_id"
    receiver_email="sonam_skills@pw.live"
    password="your_generated_app_password"
    # go to your google account: https://myaccount.google.com/, 
    # search for app-paasword
    # generate one password and use here
    msg=MIMEText(body)
    msg['subject']=subject
    msg["from"]=sender_email
    msg["to"]=receiver_email
    
    with smtplib.SMTP("smtp.gmail.com","587") as server:
        server.starttls() #encrypt connection
        server.login(sender_email,password)
        server.send_message(msg)
        print("Message Send Successfully")
    
send_email("Test Email",
           "Checking Mail Function")

# When you use with statement means
# opens connections and close when block ends

