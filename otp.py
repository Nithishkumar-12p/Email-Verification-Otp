import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

def otp(to_email):
    otp = random.randint(1111,9999)

    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    username = "nithishkumarbollapelli@gmail.com"
    password = "ldpq mjcf qnma rfra"

    from_email = "nithishkumarbollapelli@gmail.com"
    subject = "OTP for Verification"
    body = f"The OPT for Verirfication is {otp}"

    msg = MIMEMultipart()
    msg["From"] = from_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body,"plain"))

    server = smtplib.SMTP(smtp_server,smtp_port)
    server.starttls()
    server.login(username,password)
    server.send_message(msg)
    server.quit()
    print("Email Sent !")

    votp = int(input("Enter Otp: "))
    if votp == otp:
        print("Verification Success")
    else:
        print("Verirification Failed")
otp("paid21315.cs@rmkec.ac.in")
otp("ashoksudireddy15@gmail.com")
otp("nithishkumarbollapelli@gmail.com")

    











    
