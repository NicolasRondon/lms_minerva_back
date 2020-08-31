import requests
from django.core.mail import send_mail

def send_simple_message():

    send_mail(
        'Subject here',
        'Here is the message.',
        'postmaster@mg.motosander.com',
        ['ru6fa.test@inbox.testmail.app'],

    )
    return "Se logro"
