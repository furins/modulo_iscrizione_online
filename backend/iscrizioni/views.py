from django.shortcuts import render
import json
from django.http import JsonResponse
from uuslug import uuslug as slugify
from .models import Evento, Utente, Iscrizione, Attivita, PartecipazioneAttivita

from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_exempt
from django.db.utils import IntegrityError
from .confirm import check_token, send_confirmation_email
from django.shortcuts import redirect


def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})


def list_eventi(request):
    """Mostra l'elenco degli eventi attivi"""
    eventi = Evento.objects.filter(
        iscrizione_aperta=True,
    ).values('slug', 'nome_evento', 'descrizione', 'link', 'testo_link')

    risposta = {"eventi": [
        {
            'titolo': evt['nome_evento'],
            'descrizione': evt['descrizione'].split('\n')[0],
            'slug': evt['slug']
        } for evt in eventi
    ]}
    return JsonResponse(risposta)


def campi_form(request, slug):
    """trasmette al template le informazioni necessarie a restituire il form di iscrizione"""
    evento = Evento.objects.get(slug=slug)
    attivita = Attivita.objects.filter(
        evento=evento).order_by('inizio_attivita', 'ordine')
    attivita_previste = [{
        'pk': el.pk,
        'nome': f'{el.get_tipo_attivita_display()}: {el.nome}',
        'inizio': el.inizio_attivita,
        'descrizione': el.descrizione,
        'opzionale': el.opzionale,
        'iscritto': False
    } for el in attivita]

    risposta = {'evento': {
        'titolo': evento.nome_evento,
        'descrizione': evento.descrizione,
        'modello_form_evento': evento.modello_form_evento,
        'slug': evento.slug,
        'link': evento.link,
        'testo_link': evento.testo_link,
        'istruzioni_finali': evento.istruzioni_finali,
        'attivita': attivita_previste
    }}
    return JsonResponse(risposta)


def confirm_email(request, token):
    try:
        utente = check_token(token)
        utente.email_validata = True
        utente.save()
        return redirect('/static/#/confirmation_ok/')
    except Exception as err:
        print(err)
        return redirect('/static/#/confirmation_error/')


def truncate_string(string, size):
    return string if string is not None and len(string) <= size else string[:size]


@csrf_exempt
def subscribe(request, slug):
    """riceve l'iscrizione di un utente e la registra, o segnala eventuali incongruenze"""
    # FIXME penso che il problema con AXIOS sia che passa i campi non come post ma come corpo del testo, quindi la protezione crsf non riesce a trovarli
    dati = json.loads(request.body)
    print(dati)
    utente, _ = Utente.objects.get_or_create(email=dati.get('email'))
    evento = Evento.objects.get(slug=slug)

    # provo a iscrivere l'utente
    iscrizione = Iscrizione(
        iscritto=utente,
        evento=evento,
        iscrizione_newsletter=dati.get('iscrizione_newsletter', False),
        richiede_crediti=dati.get('desidera_crediti', False)
    )
    try:
        iscrizione.save()
    except IntegrityError as err:
        risposta = {
            'error': "Siete già iscritti all'evento"
        }
        return JsonResponse(risposta, status=409)

    # se arrivo qui allora vuol dire che l'iscrizione è andata a buon fine e posso quindi aggiornare i dati dell'utente
    # lo faccio ora perchè non voglio consentire che utenti vedano modificati i propri dati da qualcuno o anche da loro stessi
    # quando provano a re-iscriversi a un medesimo evento

    utente.nome = truncate_string(dati.get('nome'), 100)
    utente.cognome = truncate_string(dati.get('cognome'), 100)
    utente.accettazione_privacy = dati.get('accettazione_privacy', True)
    if dati.get('codice_fiscale').strip() != '':
        utente.codice_fiscale = truncate_string(dati.get('codice_fiscale'), 16)
    if dati.get('matricola_ordine').strip() != '':
        utente.matricola_ordine = truncate_string(
            dati.get('matricola_ordine'), 50)
    if dati.get('regione').strip() != '':
        utente.regione = dati.get('regione')
    if dati.get('provincia').strip() != '':
        utente.provincia = truncate_string(dati.get('provincia'), 2)
    if dati.get('ordine_di_appartenenza').strip() != '':
        utente.ordine_di_appartenenza = dati.get('ordine_di_appartenenza')
    utente.save()

    elenco_attivita = Attivita.objects.filter(id__in=dati['attivita'])

    for attivita in elenco_attivita:
        partecipazione = PartecipazioneAttivita(
            iscritto=iscrizione,
            attivita=attivita
        )
        partecipazione.save()

    send_confirmation_email(iscrizione, attivita=elenco_attivita)

    risposta = {}  # se va tutto bene non aggiungo nulla
    return JsonResponse(risposta)
