from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_welcome_email(name, reciever):
    #Creating message subject and sender

    subject = 'Welcome to the ElimishaTribune Newsletter'
    sender = 'angelscodex101@gmail.com'

    #Passing in the context variables

    text_content = render_to_string('email/newsemail.txt',{"name": name})
    html_content = render_to_string('email/newsemail.html',{"name": name})

    msg = EmailMultiAlternatives(subject, text_content, sender,[reciever])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

    