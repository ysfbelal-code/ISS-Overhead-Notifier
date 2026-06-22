import smtplib
from email.message import EmailMessage
from os import getenv

class Message(smtplib.SMTP):
    def __init__(self, host: str = "smtp.gmail.com", port: int = 587) -> None:
        super().__init__(host, port)
        self.email_sender = getenv("GMAIL_EMAIL")
        self.email_password = getenv("GMAIL_PASSWORD")
        self.email_receiver = getenv("EMAIL_RECEIVER")
        self.msg = EmailMessage()
        self.msg['Subject'] = "The ISS is over you!"
        self.msg['From'] = self.email_sender
        self.msg['To'] = self.email_receiver
        self.msg.set_content("You're just a window away from seeing the ISS over you house! Come quick before it's gone!")
        
    def send_email(self):        
        self.starttls()
        self.login(user=self.email_sender, password=self.email_password)     
        self.send_message(msg=self.msg) 
        return "Email sent!"  
