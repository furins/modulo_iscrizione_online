from django.shortcuts import render
import json
from django.http import JsonResponse
from uuslug import uuslug as slugify
from .models import Evento


def list_eventi(request):
    """Mostra l'elenco degli eventi attivi"""
    eventi = Evento.objects.filter(
        iscrizione_aperta=True,

    ).values('slug', 'nome_evento', 'descrizione')

    risposta = {"eventi": [
        {
            'titolo': evt['nome_evento'],
            'descrizione': evt['descrizione'],
            'slug': evt['slug']
        } for evt in eventi
    ]}
    return JsonResponse(risposta)


def campi_form(request, slug):
    """trasmette al template le informazioni necessarie a restituire il form di iscrizione"""
    risposta = {}
    return JsonResponse(risposta)


def subscribe(request, slug):
    """riceve l'iscrizione di un utente e la registra, o segnala eventuali incongruenze"""
    risposta = {}
    return JsonResponse(risposta)
# TODO creare campo per ricevere la risposta
