from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_activation_code(email, activation_code):
    context = {
        'text_detail': 'Спасибо за регистрацию',
        'email': email,
        'domain': 'http://localhost:8000', 
        'activation_code': activation_code
    }
    msg_htm = render_to_string('index.html', context)
    message = strip_tags(msg_htm)
    send_mail('Account activation', message, 'admin@gmail.com', [email], html_message=msg_htm, fail_silently=False)