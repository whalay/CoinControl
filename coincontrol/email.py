import os
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



def send_confirm_email(email_receiver, user, confirm_url):
    
    email_username = os.getenv("MAIL_USERNAME")
    email_password =  os.getenv("MAIL_PASSWORD")

    
    subject = "CoinControl Email Confirmation"
    html = f"""\
            <html>
            <body>
                <h3>Dear {user},</h3><br>
                <p>Thank you for registering with CoinControl. To complete the registration process and activate your account, 
                we kindly ask you to confirm your email address by clicking on the link below:</p><br>
                <p><a href="{ confirm_url }">Click here to confirm</a></p><br>
                <p>By clicking on the link, you will be directed to a confirmation page where you can verify your email address. 
                Please ensure that you complete this step to gain full access to our services.</p><br>
                <p>If you did not initiate this registration or believe this email was sent to you in error, please disregard it.</p><br>
                <p>If you have any questions or need further assistance, please do not hesitate to contact our support team at <a href="mailto:support@coincontrol.com">support@coincontrol.com</a>.</p><br>
                <p>Thank you for choosing Coincontrol. We look forward to serving you.</p><br>
                <p>Best regards,<br>
                Coincontrol Team.
                </p>
                </body>
            </html>
            """

    message = MIMEMultipart("alternative")
    message['From'] = email_username
    message['To'] = email_receiver
    message['Subject'] = subject
    
    part1 = MIMEText(html, "html")
    message.attach(part1)
    
    
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_username, email_password)
        smtp.sendmail(email_username, email_receiver, message.as_string())


def resend_confirm_email(email_receiver, user, confirm_url):
    
    email_username = os.getenv("MAIL_USERNAME")
    email_password =  os.getenv("MAIL_PASSWORD")

    
    subject = "CoinControl Resend Email Confirmation"
    html = f"""\
            <html>
            <body>
                <h3>Dear {user},</h3><br>
                <p>Thank you for registering with CoinControl. To complete the registration process and activate your account, 
                we kindly ask you to confirm your email address by clicking on the link below:</p><br>
                <p><a href="{ confirm_url }">Click here to confirm</a></p><br>
                <p>By clicking on the link, you will be directed to a confirmation page where you can verify your email address. 
                Please ensure that you complete this step to gain full access to our services.</p><br>
                <p>If you did not initiate this registration or believe this email was sent to you in error, please disregard it.</p><br>
                <p>If you have any questions or need further assistance, please do not hesitate to contact our support team at <a href="mailto:support@coincontrol.com">support@coincontrol.com</a>.</p><br>
                <p>Thank you for choosing Coincontrol. We look forward to serving you.</p><br>
                <p>Best regards,<br>
                Coincontrol Team.
                </p>
                </body>
            </html>
            """


    message = MIMEMultipart("alternative")
    message['From'] = email_username
    message['To'] = email_receiver
    message['Subject'] = subject
    
    part1 = MIMEText(html, "html")
    message.attach(part1)
    
    
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_username, email_password)
        smtp.sendmail(email_username, email_receiver, message.as_string())
        
        
def send_passwordreset_email(email_receiver, user, confirm_url):
    
    email_username = os.getenv("MAIL_USERNAME")
    email_password =  os.getenv("MAIL_PASSWORD")

    
    subject = "CoinControl Account Recovery"
    html = f"""\
        <html>
        <body
            <h3>Dear {user},</h3><br>
            <p>We have received your request for coin control recovery. 
            We understand that you are experiencing issues accessing your coins and we are here to assist you. 
            Please click the link below to initiate the recovery process</p><br>
            <p><a href="{ confirm_url }">Click here to reset your password</a></p><br>
            <p>If you have any questions or need further assistance, please do not hesitate to contact our support team at <a href="mailto:support@coincontrol.com">support@coincontrol.com</a>.</p><br>
            <p>Thank you for your patience and cooperation.</p><br>
            <p>Best regards,<br>
            Coincontrol Team.
            </p>
            </body>
        </html>
        """

    message = MIMEMultipart("alternative")
    message['From'] = email_username
    message['To'] = email_receiver
    message['Subject'] = subject
    
    part1 = MIMEText(html, "html")
    message.attach(part1)
    
    
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_username, email_password)
        smtp.sendmail(email_username, email_receiver, message.as_string())
