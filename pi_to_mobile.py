from twilio.rest import Client
import twilio_account

def main():
	client = Client(twilio_account.sid,twilio_account.auth_token)

	message = client.messages.create(
		to = twilio_account.my_phone_number,
		from_ = twilio_account.twilio_phone_number,
		body = "hello from python")

	print(message.sid)

main()
