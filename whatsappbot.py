#Every message costs 0.005$
from twilio.rest import Client

reciver = input("Enter the recivers n.o = ")
message = input("Enter the message =  ")



# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "AC8ae57f2c8712b96708cd8d588cfd68a9"
auth_token = "dcd2698ad9b2bb860ae32ef7f4c55d14"
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body = message,
                              from_="whatsapp:+14155238886",
                              to="whatsapp:"+"+91"+reciver
                          )

print(message.sid)
