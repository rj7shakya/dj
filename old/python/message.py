from twilio.rest import Client

account_sid = "AC5d2241b6ca8e3fb4d8c6f04613e4a190"
auth_token ="52546a1b4c543550e25db3a8dfd31512"
client = Client(account_sid,auth_token)

message = client.messages.create(body="hi",to="+9779860132600", from_="+17069482798")
# print(message.sid)