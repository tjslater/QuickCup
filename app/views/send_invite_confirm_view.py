from django.shortcuts import render
import pusher
from twilio.rest import TwilioRestClient

__author__ = 'Confucius'


def send_invite_confirm(request):
    # Your Account Sid and Auth Token from twilio.com/user/account
    account_sid = "ACd44c538d3c34bab8d39da1c2f852e476"
    auth_token = "75e55f7ab6c83bdfc2edebbf75e0af32"
    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.create(
        body="Hi, this is Jason Kanter. Can we meet in 90 minutes at the Starbucks near you? My number is 202-560-4930",
        to="+18045039896",
        from_="+13217326068",
        mediaUrl="http://img1.etsystatic.com/000/0/5137860/il_570xN.301880621.jpg"
    )
    print message.sid

    p = pusher.Pusher(
        app_id='54801',
        key='dff4985e70a87cb08a6d',
        secret='ed26538dfb406e95d4dc'
    )
    sender = request.session.get('profile', 'no profile')
    recipient = request.session.get('recipient', 'no recipient found')
    p[sender.linkedin].trigger('my_event',
                               {'message': "{} has invited {}".format(sender.first_name, recipient.first_name)})
    data = {"sender": sender, "recipient": recipient}
    return render(request, 'send_invite_confirm_page.html', data)