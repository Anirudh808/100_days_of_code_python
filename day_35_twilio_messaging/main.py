from twilio.rest import Client

account_sid = "ACb9014db48feb739cbb90b63cac4d1fec"
auth_token = "1c20f498b2dd6a98532c74208b076add"
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="This is the ship that made the Kessel Run in fourteen parsecs?",
    from_="+17543108129",
    to="+919345453725",
)

print(message.body)
