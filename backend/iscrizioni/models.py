from decimal import Decimal

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from uuslug import uuslug as slugify
from django.core.exceptions import ValidationError


class TipoRegione(models.TextChoices):
    ABRUZZO = "Abruzzo"
    BASILICATA = "Basilicata"
    CALABRIA = "Calabria"
    CAMPANIA = "Campania"
    EMILIA_ROMAGNA = "Emilia-Romagna"
    FRIULI_VENEZIA_GIULIA = "Friuli-Venezia Giulia"
    LAZIO = "Lazio"
    LIGURIA = "Liguria"
    LOMBARDIA = "Lombardia"
    MARCHE = "Marche"
    MOLISE = "Molise"
    PIEMONTE = "Piemonte"
    PUGLIA = "Puglia"
    SARDEGNA = "Sardegna"
    SICILIA = "Sicilia"
    TOSCANA = "Toscana"
    TRENTINO_ALTO_ADIGE = "Trentino-Alto Adige"
    UMBRIA = "Umbria"
    VALLE_D_AOSTA = "Valle d'Aosta"
    VENETO = "Veneto"


class TipoOrdine(models.TextChoices):
    INGEGNERI = "Consiglio nazionale ingegneri",
    ARCHITETTI = "Consiglio nazionale architetti, pianificatori, paesaggisti e conservatori",
    CHIMICI = "Consiglio nazionale dei chimici",
    GEOLOGI = "Consiglio nazionale dei geologi",
    BIOLOGI = "Ordine nazionale dei biologi",
    AGRONOMI = "Ordine nazionale dei dottori agronomi e dottori forestali"


class Utente(models.Model):
    """è una persona nell'archivio CIRF, che ha partecipato ad almeno un evento"""
    # FIXME eliminare email non validate se più vecchie di tot tempo?
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    azienda = models.TextField(blank=True)
    indirizzo = models.TextField(blank=True)
    telefono = models.CharField(max_length=100, blank=True)
    codice_fiscale = models.CharField(max_length=16, blank=True)
    email = models.EmailField(unique=True)
    email_validata = models.BooleanField(default=False)
    accettazione_privacy = models.BooleanField(default=False)
    ordine_di_appartenenza = models.CharField(
        max_length=73, null=True, blank=True, choices=TipoOrdine.choices
    )
    matricola_ordine = models.CharField(max_length=50, blank=True)
    regione = models.CharField(
        max_length=21, choices=TipoRegione.choices, null=True, blank=True)
    provincia = models.CharField(max_length=2, blank=True)
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

    def save(self, **kwargs):
        self.provincia = self.provincia.upper() if self.provincia is not None else None
        self.codice_fiscale = self.codice_fiscale.upper(
        ) if self.codice_fiscale is not None else None
        super(Utente, self).save(**kwargs)


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
        constraints = [
            models.UniqueConstraint(
                fields=['iscritto', 'evento'],
                name='iscrizione_ad_evento'
            )
        ]

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
    CON_ATTIVITA = 'con_attivita', _('Con selezione attività')


class Evento(models.Model):
    """è la descrizione di un evento"""
    nome_evento = models.CharField(max_length=200)
    descrizione = models.TextField(blank=True)
    link = models.URLField(blank=True)
    testo_link = models.CharField(max_length=100, blank=True)
    immagine = models.ImageField(blank=True, null=True)
    istruzioni_finali = models.TextField(
        blank=True, help_text="Inserire un testo che apparirà alla fine del form di iscrizione (opzionale)")

    istruzioni_email = models.TextField(
        blank=True, help_text="Inserire un testo che apparirà nell'email di conferma dell'iscrizione all'evento (opzionale)")

    iscrizione_aperta = models.BooleanField(default=True)
    inizio_iscrizioni = models.DateTimeField(blank=True, null=True)
    termine_iscrizioni = models.DateTimeField(blank=True, null=True)

    richiede_autenticazione = models.BooleanField(
        default=False, help_text="spuntare questa casella se si desidera che l'utente possa accedere a una pagina dove potrà gestire la propria iscrizione, ad esempio per inviare un abstract")

    # slug viene usato per creare l'url dell'evento
    slug = models.SlugField(max_length=30, unique=True, blank=True)

    # modello_form_evento è un descrittore per capire quale template usare per il form di iscrizione all'evento o per le pagine di supporto (landing page, descrizione...)
    modello_form_evento = models.CharField(
        max_length=20, choices=TemplateEvento.choices, default="default")

    class Meta:
        verbose_name_plural = 'Eventi'
        ordering = ['-inizio_iscrizioni']

    def save(self, **kwargs):
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
    ordine = models.CharField(
        max_length=73, choices=TipoOrdine.choices
    )
    regione = models.CharField(
        max_length=21, choices=TipoRegione.choices, blank=True, help_text="lasciare vuoto per indicare tutte le regioni")
    istruzioni = models.TextField(
        blank=True, help_text="il testo verrà inserito nell'email di conferma iscrizione ed eventualmente ripetuto in email successive solo per gli utenti iscritti a questo evento e appartenenti a quest'ordine professionale.")

    class Meta:
        verbose_name_plural = 'accreditamenti ordini'

    def __str__(self):
        return f"{self.ordine} della regione {self.regione} per l'evento {self.evento}"


class TipoAttivita(models.TextChoices):
    SEMINARIO = 'seminario', _('Seminario')
    WORKSHOP = 'workshop', _('Workshop')
    WEBINAR = 'webinar', _('Webinar')
    PRANZO_SOCIALE = 'pranzo_sociale', _('Pranzo sociale')
    FIELD_TRIP = 'field_trip', _('Field trip')


class Attivita(models.Model):
    nome = models.CharField(max_length=100)
    tipo_attivita = models.CharField(
        max_length=20, choices=TipoAttivita.choices, default=TipoAttivita.SEMINARIO)
    evento = models.ForeignKey('Evento', on_delete=models.CASCADE)

    descrizione = models.TextField(blank=True)
    istruzioni_email = models.TextField(
        blank=True, help_text="Inserire un testo che apparirà nell'email di conferma dell'iscrizione all'evento (opzionale). Può essere usata per indicare la password del webinar. Per il link invece usare l'apposita casella qui sotto.")
    link = models.URLField(blank=True)
    testo_link = models.CharField(max_length=100, blank=True)
    mostra_link_nel_modulo_iscrizione = models.BooleanField(
        default=False, help_text="mostrandolo nel modulo di iscrizione, sarà accessibile a tutti, anche i non iscritti. Normalmente è bene che non sia spuntata questa casella.")

    inizio_attivita = models.DateTimeField(null=True, blank=True)
    termine_attivita = models.DateTimeField(null=True, blank=True)
    crediti_riconosciuti = models.BooleanField(
        default=True, help_text="I crediti verranno riconosciuti solo se sono previsti anche a livello di evento. Normalmente è sicuro lasciare questa casella spuntata.")
    valore_crediti_riconosciuti = models.DecimalField(
        max_digits=5, decimal_places=2, default=Decimal(1.0), blank=True)
    opzionale = models.BooleanField(default=True)
    ordine = models.IntegerField(
        blank=True, default=0, help_text="Se due attività hanno la stessa data/ora, mostra prima quella che avrà il valore 'ordine' più basso.")

    def __str__(self):
        return f'{self.get_tipo_attivita_display()} "{self.nome}" durante "{self.evento.nome_evento}"'

    class Meta:
        verbose_name = 'attività'
        verbose_name_plural = "attività"


class PartecipazioneAttivita(models.Model):
    iscritto = models.ForeignKey('Iscrizione', on_delete=models.CASCADE)
    attivita = models.ForeignKey('Attivita', on_delete=models.CASCADE)
    data_iscrizione = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"iscrizione di {self.iscritto.iscritto} al {self.attivita}"

    def clean(self):
        if self.iscritto.evento != self.attivita.evento:
            raise ValidationError(
                f"l'utente {self.iscritto.iscritto} non è iscritto all'evento in cui è prevista questa attività ({self.attivita.evento})")
        super(PartecipazioneAttivita, self).clean()

    class Meta:
        verbose_name = 'iscrizione singola attività'
        verbose_name_plural = "iscrizioni singola attività"
