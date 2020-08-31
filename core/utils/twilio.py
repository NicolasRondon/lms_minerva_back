from twilio.rest import Client

from lms_minerva.settings import account_twilio, token_twilio

account = account_twilio
token = token_twilio
client = Client(account, token)


def send_sms(name, code):
    from_whatsapp_number='+12818017336'
    to_whatsapp_number='+573208039305'
    client.messages.create(
    body="Hola {}, gracias por ser parte de Minerva tu código de confirmacion es: {}".format(name, code),
    from_=from_whatsapp_number,
    to=to_whatsapp_number
    )

    return
