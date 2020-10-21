
from twilio.rest import Client
import schedule
import time
# 1. preset message (use string)
# 2. sent message (wll prob use twilio)
# 3. Schedule message (Windows scheduler?)

receiver_number = "Verified receiver number"
sender_number = "Twilio sender number"
message = "Example message"


def send_message():
    account_sid = "ACCOUNT ID"
    auth_token = "TOKEN"
    client = Client(account_sid, auth_token)
    returned_message = client.messages.create(
        to=receiver_number,
        from_=sender_number,
        body=message)

    print(returned_message.sid)


send_message()
schedule.every().day.at("10:00").do(send_message)
while True:
    schedule.run_pending()
    time.sleep(1)

