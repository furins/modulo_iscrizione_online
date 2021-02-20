from django.contrib import admin
from .models import Evento, Utente, Iscrizione


@admin.register(Utente)
class UtenteAdmin(admin.ModelAdmin):
    list_display = ('cognome', 'nome', 'email', 'telefono',
                    'email_validata', 'ultima_modifica')


@admin.register(Iscrizione)
class IscrizioneAdmin(admin.ModelAdmin):
    def get_cognome(self, obj):
        return obj.iscritto.cognome
    get_cognome.admin_order_field = 'iscritto__cognome'
    get_cognome.short_description = 'cognome'

    def get_nome(self, obj):
        return obj.iscritto.nome
    get_cognome.admin_order_field = 'iscritto__nome'
    get_cognome.short_description = 'nome'

    list_display = ('get_cognome', 'get_nome', 'evento',
                    'pagamento_ricevuto', 'data_iscrizione', 'iscrizione_newsletter')
    list_select_related = ('iscritto',)
    list_filter = ('evento', 'pagamento_ricevuto', 'iscrizione_newsletter')


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nome_evento', 'iscrizione_aperta')
