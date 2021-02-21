from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from django.utils.http import base36_to_int, int_to_base36, urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.crypto import salted_hmac
from django.conf import settings
from .models import Iscrizione


def hash_string_generator(iscrizione):
    return salted_hmac(
        "modulo_iscrizione_online.token",
        f'{iscrizione.iscritto.pk}-{iscrizione.evento.pk}',
        secret=settings.SECRET_KEY
    ).hexdigest()


def token_generator(iscrizione):
    email_b64 = urlsafe_base64_encode(iscrizione.iscritto.email.encode())
    iscrizione_b36 = int_to_base36(iscrizione.pk)

    return f'{email_b64}-{iscrizione_b36}-{hash_string_generator(iscrizione)}'


def check_token(token):
    email, iscrizione_pk, hash_string = token.split('-')
    email = urlsafe_base64_decode(email).decode()
    iscrizione_pk = base36_to_int(iscrizione_pk)

    iscrizione = Iscrizione.objects.get(pk=iscrizione_pk)
    if hash_string_generator(iscrizione) != hash_string:
        raise ValueError
    return iscrizione.iscritto


def send_confirmation_email(iscrizione):
    context = {
        'iscrizione': iscrizione,
        'token': token_generator(iscrizione),
        'dominio': settings.SITE_URL
    }

    text = render_to_string('email/confirmation.txt', context)
    html = render_to_string('email/confirmation.html', context)

    msg = EmailMultiAlternatives(
        f"Conferma iscrizione a {iscrizione.evento.nome_evento}",
        text,
        settings.EMAIL_HOST_USER,
        [iscrizione.iscritto.email]
    )
    msg.attach_alternative(html, 'text/html')
    msg.send()
