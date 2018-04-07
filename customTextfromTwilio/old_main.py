# SETUP
import parse
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC9b5b706a81c3989817ad2b4182f5c287"
# Your Auth Token from twilio.com/console
auth_token = 

client = Client(account_sid, auth_token)

# get the phone number
rawphone = raw_input("Please input a phone number: ")

# Parse the phone number
fixedphone = parse.parse(rawphone)
print("That's ", fixedphone, "to be E.164 compliant")

# Get the message
mess = raw_input("What's your message?\n")

# Finally Send the message
message = client.messages.create(
    to=fixedphone,
    from_="+16504603660",
    body=mess)

print(message.sid)
print("Message Sent")