# Generated by Django 3.1.7 on 2021-02-20 10:06

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attivita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descrizione', models.TextField()),
                ('inizio_attivita', models.DateTimeField(null=True)),
                ('termine_attivita', models.DateTimeField(null=True)),
                ('crediti_riconosciuti', models.DecimalField(decimal_places=2, max_digits=5)),
                ('opzionale', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inizio_iscrizioni', models.DateTimeField(null=True)),
                ('termine_iscrizioni', models.DateTimeField(null=True)),
                ('iscrizione_aperta', models.BooleanField(default=True)),
                ('richiede_autenticazione', models.BooleanField(default=False)),
                ('nome_evento', models.CharField(max_length=200)),
                ('descrizione', models.TextField(blank=True)),
                ('immagine', models.ImageField(null=True, upload_to='')),
                ('slug', models.SlugField(max_length=20, unique=True)),
                ('modello_form_evento', models.CharField(blank=True, max_length=20)),
                ('link', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ordine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Regione',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Utente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cognome', models.CharField(max_length=100)),
                ('azienda', models.TextField(blank=True)),
                ('indirizzo', models.TextField(blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('matricola_ordine', models.CharField(blank=True, max_length=50)),
                ('provincia', models.CharField(blank=True, max_length=50)),
                ('ultima_modifica', models.DateTimeField(auto_now_add=True)),
                ('accettazione_privacy', models.BooleanField(default=False)),
                ('ordine_di_appartenenza', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='iscrizioni.ordine')),
                ('regione', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='iscrizioni.regione')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PrezzoEvento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('importo', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=5)),
                ('riservato_ai_soci', models.BooleanField(default=False)),
                ('tempo_limitato', models.BooleanField(default=False)),
                ('sconto_categoria', models.BooleanField(default=False)),
                ('opzionale', models.BooleanField(default=False)),
                ('descrizione', models.TextField()),
                ('inizio_validita', models.DateTimeField(null=True)),
                ('termine_validita', models.DateTimeField(null=True)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iscrizioni.evento')),
            ],
        ),
        migrations.CreateModel(
            name='PartecipazioneAttivita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_partecipazione', models.DateTimeField(auto_now_add=True)),
                ('attivita', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iscrizioni.attivita')),
                ('iscritto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iscrizioni.utente')),
            ],
        ),
        migrations.CreateModel(
            name='NotificheAzioneEvento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_azione', models.CharField(choices=[('I', 'Iscrizione'), ('D', 'Disiscrizione'), ('F', 'Invio documento'), ('P', 'Invio ricevuta di pagamento')], max_length=1)),
                ('email', models.EmailField(max_length=254)),
                ('messaggio', models.TextField()),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iscrizioni.evento')),
            ],
        ),
        migrations.CreateModel(
            name='Iscrizione',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_interne', models.TextField(blank=True, help_text="Queste note non saranno mai visibili all'utente")),
                ('richieste_dell_iscritto', models.TextField(blank=True)),
                ('pagamento_ricevuto', models.BooleanField(default=False)),
                ('importo_ricevuto', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=5)),
                ('data_iscrizione', models.DateTimeField(auto_now_add=True)),
                ('data_pagamento', models.DateTimeField(null=True)),
                ('richiede_crediti', models.BooleanField(default=False)),
                ('iscrizione_newsletter', models.BooleanField(default=None, null=True)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iscrizioni.evento')),
                ('iscritto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iscrizioni.utente')),
            ],
        ),
        migrations.AddField(
            model_name='attivita',
            name='evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iscrizioni.evento'),
        ),
        migrations.CreateModel(
            name='AllegatoIscrizione',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allegato', models.FileField(null=True, upload_to='')),
                ('allegato_testuale', models.TextField(blank=True)),
                ('tipo_allegato', models.CharField(choices=[('T', 'Testo'), ('F', 'File'), ('P', 'Ricevuta di pagamento')], max_length=1)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iscrizioni.evento')),
                ('iscritto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iscrizioni.utente')),
            ],
        ),
        migrations.CreateModel(
            name='AllegatiPossibili',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_allegato', models.CharField(max_length=200)),
                ('descrizione', models.TextField(blank=True)),
                ('opzionale', models.BooleanField(default=False)),
                ('richiesto_all_iscrizione', models.BooleanField(default=False)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iscrizioni.evento')),
            ],
        ),
        migrations.CreateModel(
            name='AccreditamentoOrdine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('istruzioni', models.TextField(blank=True)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iscrizioni.evento')),
                ('ordine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iscrizioni.ordine')),
                ('regione', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iscrizioni.regione')),
            ],
        ),
    ]
