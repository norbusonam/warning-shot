from twilio.rest import Client

def send_message(location):

    account_sid = "AC06cf139374327be6c8401c39afacb507"
    auth_token = "641dddfb20d8d4069bebc652d0ab46ec"

    client = Client(account_sid, auth_token)
    
    client.messages.create(
        to = "+15082809733",
        from_ = "+17636007661",
        body = "(UNCONFIRMED) Gunfire detected in {}.".format(location)
    )

