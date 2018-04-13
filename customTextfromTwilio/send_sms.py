def send(mess,phone):

    #INPUT is expected to be an E.164 compliant phone number
    #Message should be a string
    #Setup
    from twilio.rest import Client

    # Your Account SID from twilio.com/console
    account_sid = "AC9b5b706a81c3989817ad2b4182f5c287"
    # Your Auth Token from twilio.com/console
    auth_token  = "6e7267c2de45d86714093fd82c4419b1"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=phone,
        from_="+16504603660",
        body=mess)

    print(message.sid)
    print("Message Sent!")