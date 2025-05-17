import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Your credentials
sender_email = "omh4453@gmail.com"
app_password = ""
x={"hariom993126@gmail.com"}
for receiver_email in x:
    print(receiver_email)

# Email content
subject = "Test Email from Python"
body = "Hello! 👋 This is a test email for 2 sent using Python,hi what is your name."

# Setup the MIME
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

message.attach(MIMEText(body, "plain"))

# Connect to Gmail SMTP server and send email
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, app_password)
    server.send_message(message)
    server.quit()
    print("✅ Email sent successfully!")
except Exception as e:
    print("❌ Failed to send email:", e)
