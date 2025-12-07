import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, app_password, receiver_email, subject, message):
    try:
        # Create mail structure
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject

        msg.attach(MIMEText(message, "plain"))

        # Connect to Gmail server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        # Login using app password
        server.login(sender_email, app_password)

        # Send email
        server.send_message(msg)
        server.quit()

        print("✅ Email sent successfully!")

    except Exception as e:
        print("❌ Email failed:", e)


# -------- MAIN PROGRAM --------
print("\n--- Auto Email Sender ---")

sender = input("Enter your Gmail: ")
app_pass = input("Enter your Gmail App Password: ")
receiver = input("Enter Receiver Email: ")
subject = input("Enter subject: ")
message = input("Enter message: ")

send_email(sender, app_pass, receiver, subject, message)