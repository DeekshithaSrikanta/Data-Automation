import pywhatkit as kit

print("\n--- Auto WhatsApp Message Sender ---")

# Phone number with country code (+91 for India)
number = input("Enter phone number (e.g., +91xxxxxxxxxx): ")

message = input("Enter message: ")

print("\nTime Format (24-hour):")
hour = int(input("Enter hour (0-23): "))
minute = int(input("Enter minute (0-59): "))

try:
    kit.sendwhatmsg(number, message, hour, minute)
    print("\n✅ Message Scheduled Successfully!")
    print("WhatsApp Web will open automatically at the scheduled time.")

except Exception as e:
    print("\n❌ Failed to send message:", e)