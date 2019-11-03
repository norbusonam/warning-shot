from twilio.rest import Client

def send_alert(location):

    account_sid = "SID"
    auth_token = "AUTH TOKEN"

    client = Client(account_sid, auth_token)
    
    client.messages.create(
        to = "NUM",
        from_ = "NUM",
        body = "(UNCONFIRMED) Gunfire detected in {}.".format(location)
    )

def send_alert_confirmation(location):

    account_sid = "SID"
    auth_token = "AUTH TOKEN"

    client = Client(account_sid, auth_token)
    
    client.messages.create(
        to = "NUM",
        from_ = "NUM",
        body = "(CONFIRMED) Gunfire detected in {}.".format(location)
    )

def send_false_alarm():

    account_sid = "SID"
    auth_token = "AUTH TOKEN"

    client = Client(account_sid, auth_token)
    
    client.messages.create(
        to = "NUM",
        from_ = "NUM",
        body = "(FALSE ALARM) Previous message was a false alarm."
    )

