import os
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(email_receiver, confirm_url):
    
    email_username = os.getenv("MAIL_USERNAME")
    email_password =  os.getenv("MAIL_PASSWORD")

    subject = "CoinControl Email Confirmation"
    message = MIMEMultipart("alternative")
    message['From'] = email_username
    message['To'] = email_receiver
    message['Subject'] = subject
    
    text = """\
        Thank you for registering with CoinControl
        """
    html = f"""\
        <html>
        <body>
            <p>Hi,<br>
            How are you?<br>
            <p>Welcome! Thanks for signing up. Please follow this link to activate your account:</p><br>
            <p><a href="{ confirm_url }">{ confirm_url }</a></p>
            </p>
        </body>
        </html>
        """
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    
    message.attach(part1)
    message.attach(part2)
    
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_username, email_password)
        smtp.sendmail(email_username, email_receiver, message.as_string())

