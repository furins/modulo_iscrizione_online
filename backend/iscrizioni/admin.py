from django.contrib import admin
from .models import Evento, Utente, Iscrizione, AccreditamentoOrdine, Attivita, PartecipazioneAttivita
from django.db import models
from django.forms import Textarea
import import_export
from import_export.admin import ExportMixin
from import_export import resources
from import_export.fields import Field
from import_export.widgets import BooleanWidget


@admin.register(Utente)
class UtenteAdmin(admin.ModelAdmin):
    list_display = ('cognome', 'nome', 'email', 'telefono',
                    'email_validata', 'ultima_modifica')
    search_fields = ['nome', 'cognome']


class CustomBooleanWidget(BooleanWidget):
    def render(self, value, obj=None):
        return "Si" if value else "No"


class IscrizioneResource(resources.ModelResource):
    iscritto__nome = Field(
        attribute='iscritto__nome', column_name='Nome')
    iscritto__cognome = Field(
        attribute='iscritto__cognome', column_name='Cognome')
    iscritto__email = Field(
        attribute='iscritto__email', column_name='Email')
    richiede_crediti = Field(
        attribute='richiede_crediti', column_name='Desidera crediti',
        widget=CustomBooleanWidget())
    iscritto__codice_fiscale = Field(
        attribute='iscritto__codice_fiscale', column_name='Cod.Fisc.')
    iscritto__ordine_di_appartenenza = Field(
        attribute='iscritto__ordine_di_appartenenza', column_name='Ordine')
    iscritto__matricola_ordine = Field(
        attribute='iscritto__matricola_ordine', column_name='Matricola ordine')
    iscritto__regione = Field(
        attribute='iscritto__regione', column_name='Regione')
    iscritto__provincia = Field(
        attribute='iscritto__provincia', column_name='Provincia')

    class Meta:
        model = Iscrizione
        fields = ('iscritto__nome', 'iscritto__cognome',
                  'iscritto__email', 'richiede_crediti',
                  'iscritto__codice_fiscale', 'iscritto__ordine_di_appartenenza',
                  'iscritto__matricola_ordine', 'iscritto__regione', 'iscritto__provincia')


class AttivitaPartecipateInline(admin.TabularInline):
    model = PartecipazioneAttivita
    readonly_fields = ('attivita',)
    extra = 0

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Iscrizione)
class IscrizioneAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = IscrizioneResource
    inlines = (AttivitaPartecipateInline,)
    formats = [
        # import_export.formats.base_formats.CSV,
        import_export.formats.base_formats.XLS,
        # import_export.formats.base_formats.XLSX
    ]

    def get_cognome(self, obj):
        return obj.iscritto.cognome
    get_cognome.admin_order_field = 'iscritto__cognome'
    get_cognome.short_description = 'cognome'

    def get_nome(self, obj):
        return obj.iscritto.nome
    get_nome.admin_order_field = 'iscritto__nome'
    get_nome.short_description = 'nome'

    list_display = ('get_cognome', 'get_nome', 'evento',
                    'pagamento_ricevuto', 'data_iscrizione', 'iscrizione_newsletter')
    list_select_related = ('iscritto',)
    list_filter = ('evento', 'pagamento_ricevuto', 'iscrizione_newsletter')
    search_fields = ['iscritto__nome', 'iscritto__cognome']

    class Media:
        css = {"all": ("/css/nascondi_inline_info.css",)}


class AccreditamentoOrdineInline(admin.TabularInline):
    model = AccreditamentoOrdine
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 1, 'cols': 80})},
    }


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nome_evento', 'iscrizione_aperta')
    list_editable = ('iscrizione_aperta',)
    inlines = (AccreditamentoOrdineInline,)

    # FIXME vanno implementati in futuro
    exclude = ('immagine', 'inizio_iscrizioni',
               'termine_iscrizioni', 'richiede_autenticazione')


class UtentiPartecipantiInline(admin.TabularInline):
    model = PartecipazioneAttivita
    readonly_fields = ('iscritto',)
    extra = 0

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Attivita)
class AttivitaAdmin(admin.ModelAdmin):
    inlines = (UtentiPartecipantiInline, )


class PartecipazioneAttivitaResource(resources.ModelResource):
    iscritto__iscritto__nome = Field(
        attribute='iscritto__iscritto__nome', column_name='Nome')
    iscritto__iscritto__cognome = Field(
        attribute='iscritto__iscritto__cognome', column_name='Cognome')
    iscritto__iscritto__email = Field(
        attribute='iscritto__iscritto__email', column_name='Email')
    iscritto__richiede_crediti = Field(
        attribute='iscritto__richiede_crediti', column_name='Desidera crediti',
        widget=CustomBooleanWidget())
    iscritto__iscritto__codice_fiscale = Field(
        attribute='iscritto__iscritto__codice_fiscale', column_name='Cod.Fisc.')
    iscritto__iscritto__ordine_di_appartenenza = Field(
        attribute='iscritto__iscritto__ordine_di_appartenenza', column_name='Ordine')
    iscritto__iscritto__matricola_ordine = Field(
        attribute='iscritto__iscritto__matricola_ordine', column_name='Matricola ordine')
    iscritto__iscritto__regione = Field(
        attribute='iscritto__iscritto__regione', column_name='Regione')
    iscritto__iscritto__provincia = Field(
        attribute='iscritto__iscritto__provincia', column_name='Provincia')
    attivita__tipo_attivita = Field(
        attribute='attivita__tipo_attivita', column_name='Tipo Attività')
    attivita__nome = Field(
        attribute='attivita__nome', column_name='Attività')
    attivita__evento__nome = Field(
        attribute='attivita__evento__nome', column_name='Evento')

    class Meta:
        model = PartecipazioneAttivita
        fields = ('iscritto__iscritto__nome', 'iscritto__iscritto__cognome',
                  'iscritto__iscritto__email', 'iscritto__richiede_crediti',
                  'iscritto__iscritto__codice_fiscale', 'iscritto__iscritto__ordine_di_appartenenza',
                  'iscritto__iscritto__matricola_ordine', 'iscritto__iscritto__regione', 'iscritto__iscritto__provincia',
                  'attivita__nome', 'attivita__tipo_attivita', 'attivita__evento__nome')


@admin.register(PartecipazioneAttivita)
class PartecipazioneAttivitaAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('get_nome_iscritto', 'get_evento', 'get_attivita')
    list_select_related = ('iscritto',)
    resource_class = PartecipazioneAttivitaResource

    def get_nome_iscritto(self, obj):
        return obj.iscritto.iscritto
    get_nome_iscritto.admin_order_field = 'iscritto__iscritto'
    get_nome_iscritto.short_description = 'iscritto'

    def get_evento(self, obj):
        return obj.iscritto.evento
    get_evento.admin_order_field = 'iscritto__evento'
    get_evento.short_description = 'evento'

    def get_attivita(self, obj):
        return f'{obj.attivita.get_tipo_attivita_display()} "{obj.attivita.nome}"'
    get_attivita.admin_order_field = 'attivita__nome'
    get_attivita.short_description = 'attivita'

    list_filter = ('attivita', 'attivita__evento')
    search_fields = ['iscritto__iscritto__nome', 'iscritto__iscritto__cognome']

    formats = [
        # import_export.formats.base_formats.CSV,
        import_export.formats.base_formats.XLS,
        # import_export.formats.base_formats.XLSX
    ]

# @admin.register(AccreditamentoOrdine)
# class AccreditamentoOrdineAdmin(admin.ModelAdmin):
#     list_display = ('ordine', 'regione', 'evento')
