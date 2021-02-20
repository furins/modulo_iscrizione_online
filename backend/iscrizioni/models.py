from decimal import Decimal

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from uuslug import uuslug as slugify
from django.core.exceptions import ValidationError


class Utente(models.Model):
    """è una persona nell'archivio CIRF, che ha partecipato ad almeno un evento"""
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    azienda = models.TextField(blank=True)
    indirizzo = models.TextField(blank=True)
    telefono = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    email_validata = models.BooleanField(default=False)
    accettazione_privacy = models.BooleanField(default=False)
    ordine_di_appartenenza = models.ForeignKey(
        'Ordine', on_delete=models.SET_NULL, null=True, blank=True)
    matricola_ordine = models.CharField(max_length=50, blank=True)
    regione = models.ForeignKey(
        'Regione', on_delete=models.SET_NULL, null=True, blank=True)
    provincia = models.CharField(max_length=50, blank=True)
    ultima_modifica = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, null=True, blank=True)  # nel caso si desideri dare accesso all'utente ad un area riservata

    class Meta:
        verbose_name = 'utente registrato'
        verbose_name_plural = 'utenti registrati'
        ordering = ['cognome', 'nome']

    def clean(self):
        # Non posso autorizzare il salvataggio se non è stata autorizzata la clausola sulla privacy.
        if self.accettazione_privacy == False:
            raise ValidationError(
                _('È necessario accettare la clausola relativa alla privacy.'))

    def __str__(self):
        return f'{self.cognome} {self.nome}'


class Iscrizione(models.Model):
    """è l'iscrizione di una persona a un evento"""
    iscritto = models.ForeignKey('Utente', on_delete=models.CASCADE)
    evento = models.ForeignKey('Evento', on_delete=models.CASCADE)
    note_interne = models.TextField(
        blank=True, help_text="Queste note non saranno mai visibili all'utente")
    richieste_dell_iscritto = models.TextField(blank=True)
    pagamento_ricevuto = models.BooleanField(default=False)
    importo_ricevuto = models.DecimalField(
        max_digits=5, decimal_places=2, default=Decimal(0.0), blank=True)
    data_iscrizione = models.DateTimeField(auto_now_add=True)
    data_pagamento = models.DateTimeField(null=True, blank=True)
    richiede_crediti = models.BooleanField(default=False)
    iscrizione_newsletter = models.BooleanField(default=None, null=True)

    class Meta:
        verbose_name_plural = 'iscrizioni'
        ordering = ['iscritto__cognome', 'iscritto__nome']

    def __str__(self):
        return f'Iscrizione di {self.iscritto} all\'evento {self.evento}'


class AllegatiPossibili(models.Model):
    nome_allegato = models.CharField(max_length=200)
    evento = models.ForeignKey('Evento', on_delete=models.CASCADE)
    descrizione = models.TextField(blank=True)
    # se opzionale = True, è un documento da allegare sempre
    opzionale = models.BooleanField(default=False)
    # se richiesto_all_iscrizione = True, l'iscrizione non è valida se non è presente questo allegato
    richiesto_all_iscrizione = models.BooleanField(default=False)


class TipoAllegato(models.TextChoices):
    TESTO = 'T', _('Testo')
    FILE = 'F', _('File')
    RICEVUTA_PAGAMENTO = 'P', _('Ricevuta di pagamento')


class AllegatoIscrizione(models.Model):
    iscritto = models.ForeignKey('Utente', on_delete=models.CASCADE)
    evento = models.ForeignKey('Evento', on_delete=models.CASCADE)
    allegato = models.FileField(null=True)
    allegato_testuale = models.TextField(blank=True)
    tipo_allegato = models.CharField(
        max_length=1, choices=TipoAllegato.choices
    )


class TemplateEvento(models.TextChoices):
    DEFAULT = 'default', _('Default')


class Evento(models.Model):
    """è la descrizione di un evento"""
    nome_evento = models.CharField(max_length=200)
    descrizione = models.TextField(blank=True)

    iscrizione_aperta = models.BooleanField(default=True)
    inizio_iscrizioni = models.DateTimeField(blank=True, null=True)
    termine_iscrizioni = models.DateTimeField(blank=True, null=True)

    richiede_autenticazione = models.BooleanField(
        default=False, help_text="spuntare questa casella se si desidera che l'utente possa accedere a una pagina dove potrà gestire la propria iscrizione, ad esempio per inviare un abstract")

    immagine = models.ImageField(blank=True, null=True)
    # slug viene usato per creare l'url dell'evento
    slug = models.SlugField(max_length=30, unique=True, blank=True)

    # modello_form_evento è un descrittore per capire quale template usare per il form di iscrizione all'evento o per le pagine di supporto (landing page, descrizione...)
    modello_form_evento = models.CharField(
        max_length=20, choices=TemplateEvento.choices, default="default")
    link = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = 'Eventi'
        ordering = ['-inizio_iscrizioni']

    def save(self, **kwargs):
        self.slug = slugify(self.nome_evento, instance=self)
        super(Evento, self).save(**kwargs)

    def __str__(self):
        return self.nome_evento


class TipoAzione(models.TextChoices):
    ISCRIZIONE = 'I', _('Iscrizione')
    DISCRIZIONE = 'D', _('Disiscrizione')
    INVIO_FILE = 'F', _('Invio documento')
    INVIO_PAGAMENTO = 'P', _('Invio ricevuta di pagamento')


class NotificheAzioneEvento(models.Model):
    """chi deve essere notificato in caso di attività connessa a evento"""
    evento = models.ForeignKey('Evento', on_delete=models.CASCADE)
    tipo_azione = models.CharField(
        max_length=1, choices=TipoAzione.choices
    )
    email = models.EmailField()
    messaggio = models.TextField()

# TODO potrebbe essere utile inserire un programma


class PrezzoEvento(models.Model):
    """è il prezzo per partecipare a un evento o a parte di esso"""
    evento = models.ForeignKey('Evento', on_delete=models.CASCADE)
    importo = models.DecimalField(
        max_digits=5, decimal_places=2, default=Decimal(0.0))
    riservato_ai_soci = models.BooleanField(default=False)
    tempo_limitato = models.BooleanField(default=False)
    sconto_categoria = models.BooleanField(default=False)
    opzionale = models.BooleanField(default=False)
    descrizione = models.TextField()
    inizio_validita = models.DateTimeField(null=True)
    termine_validita = models.DateTimeField(null=True)


class AccreditamentoOrdine(models.Model):
    evento = models.ForeignKey('Evento', on_delete=models.CASCADE)
    ordine = models.ForeignKey('Ordine', on_delete=models.CASCADE)
    regione = models.ForeignKey('Regione', on_delete=models.CASCADE)
    istruzioni = models.TextField(blank=True)


class Attivita(models.Model):
    nome = models.CharField(max_length=100)
    descrizione = models.TextField()
    evento = models.ForeignKey('Evento', on_delete=models.CASCADE)
    inizio_attivita = models.DateTimeField(null=True)
    termine_attivita = models.DateTimeField(null=True)
    crediti_riconosciuti = models.DecimalField(max_digits=5, decimal_places=2)
    opzionale = models.BooleanField(default=False)


class PartecipazioneAttivita(models.Model):
    iscritto = models.ForeignKey('Utente', on_delete=models.CASCADE)
    attivita = models.ForeignKey('Attivita', on_delete=models.CASCADE)
    data_partecipazione = models.DateTimeField(auto_now_add=True)


class Ordine(models.Model):
    nome = models.CharField(max_length=100)


class Regione(models.Model):
    nome = models.CharField(max_length=30)
