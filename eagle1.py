from twilio.rest import Client

from secrets import account_sid, auth_token, ToNumber, FromNumber

def sendMessage():
	client = Client(account_sid, auth_token)

	message = client.messages.create(
    		to=ToNumber, 
    		from_=FromNumber,
    		body="Basanese.com is down....")


