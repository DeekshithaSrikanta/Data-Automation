import os
import shutil
import smtplib
import pywhatkit as kit
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# -------------------------------------------
# 1️⃣ FILE ORGANIZER
# -------------------------------------------
def organize_files(folder):
    extensions = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Videos": [".mp4", ".mkv", ".avi"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
        "Apps": [".exe", ".msi", ".apk"],
        "Music": [".mp3", ".wav"]
    }

    files = os.listdir(folder)

    for file in files:
        file_path = os.path.join(folder, file)

        if os.path.isdir(file_path):
            continue

        ext = os.path.splitext(file)[1].lower()

        moved = False
        for category, ext_list in extensions.items():
            if ext in ext_list:
                category_folder = os.path.join(folder, category)
                os.makedirs(category_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(category_folder, file))
                moved = True
                break

        if not moved:
            other_folder = os.path.join(folder, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, file))

    print("✅ Files organized successfully!")


# -------------------------------------------
# 2️⃣ AUTO EMAIL SENDER
# -------------------------------------------
def send_email(sender_email, sender_password, receiver_email, subject, message):
    try:
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg["Subject"] = subject

        msg.attach(MIMEText(message, "plain"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()

        print("✅ Email Sent Successfully!")

    except Exception as e:
        print("❌ Email Failed:", e)


# -------------------------------------------
# 3️⃣ AUTO WHATSAPP MESSAGE SENDER
# -------------------------------------------
def send_whatsapp(number, message, hour, minute):
    try:
        kit.sendwhatmsg(number, message, hour, minute)
        print("✅ WhatsApp message scheduled successfully!")

    except Exception as e:
        print("❌ Failed to send WhatsApp message:", e)


# -------------------------------------------
# MENU
# -------------------------------------------
print("\n==============================")
print("   PYTHON AUTOMATION SUITE")
print("==============================")
print("1. Organize Files")
print("2. Send Email")
print("3. Send WhatsApp Message")
print("==============================")

choice = int(input("Choose an option: "))

if choice == 1:
    folder = input("Enter folder path to organize: ")
    organize_files(folder)

elif choice == 2:
    sender = input("Enter your Gmail: ")
    password = input("Enter App Password (not Gmail password): ")
    receiver = input("Enter Receiver Email: ")
    subject = input("Subject: ")
    message = input("Message: ")
    send_email(sender, password, receiver, subject, message)

elif choice == 3:
    number = input("Enter phone number (+91xxxxxxxxxx): ")
    message = input("Enter message: ")
    hour = int(input("Hour (24-hr format): "))
    minute = int(input("Minute: "))
    send_whatsapp(number, message, hour, minute)

else:
    print("❌ Invalid choice!")