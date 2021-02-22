from django.contrib import admin
from .models import Evento, Utente, Iscrizione, AccreditamentoOrdine
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


@admin.register(Iscrizione)
class IscrizioneAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = IscrizioneResource
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


# @admin.register(AccreditamentoOrdine)
# class AccreditamentoOrdineAdmin(admin.ModelAdmin):
#     list_display = ('ordine', 'regione', 'evento')
