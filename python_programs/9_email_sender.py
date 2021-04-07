import yagmail

gmail = ""
password = ""
recipients = ""

# read the Gmail account from the file where it is stored
with open("/home/pi/.local/share/.gmail_account", "r") as f:
    gmail = f.read()

# read the email password from the file where it is stored
with open("/home/pi/.local/share/.email_password", "r") as f:
    password = f.read()

# readthe email recipients from the file where they are stored
# return all lines in the file, as a list where each line is an item in this list
with open("/home/pi/.local/share/.email_recipients", "r") as f:
    recipients = f.readlines()

# set the Gmail account information
yag = yagmail.SMTP(gmail, password)

# set the parameters necessary for sending email
yag.send(to=recipients,
         subject="first email",
         contents="Hello from Raspberry Pi",
         # add an attachment to this email
         attachments="/home/pi/Pictures/Raspberry_Pi_Logo/RPi-Logo.png")
print("Email sent")
