import smtplib
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
def send_welcome_email(username,email):
    # Creating message subject and sender
    subject = 'Welcome to Jirani'
    sender = 'issirandom@gmail.com'

    #passing in the context vairables

    html_content = render_to_string('email.html',{"username":username})
    text_content = "Hello {{username}}, Welcome to Jirani! Jirani means neighbour. Join your hood to keep thespirit of neighborhood."
    msg = EmailMultiAlternatives(subject,text_content,sender,[email])
    msg.attach_alternative(html_content,'text/html')
    try:
        msg.send()
    except smtplib.SMTPException as e:
        print('There was an error sending an email, kindly check your email: ', e)