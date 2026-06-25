import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_python(sender_email,sender_password,receiver_email,subject,body):
    msg=MIMEMultipart()
    msg["From"]=sender_email
    msg["To"]=receiver_email
    # msg["To"]=", ".join(receiver_email)
    msg["Subject"]=subject

    msg.attach(MIMEText(body,"plain"))

    try:
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(sender_email,sender_password)
        server.sendmail(sender_email,receiver_email,msg.as_string())
        server.quit()
        print("Email Sent Successfully...")
    except Exception as e:
        print("Error :", e)
send_email_python(
    sender_email="niteshkalangada8@gmail.com",
    receiver_email="panchalnik285@gmail.com ",
    # receiver_email=["nikhilranjan2501@gmail.com",""],
    sender_password="inbj jfvp kqcf omio",
    subject="Testing Email sender Using Pure Python",
    body="Hello, kya kr rhi ho . Assignments ho gye kya sare ?"
)