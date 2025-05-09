import os

from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

account_sid = os.getenv("SID")
auth_token = os.getenv("TOKEN")
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="This is the ship that made the Kessel Run in fourteen parsecs?",
    from_="+17543108129",
    to="+919345453725",
)

print(message.body)
