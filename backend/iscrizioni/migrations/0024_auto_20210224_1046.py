# Generated by Django 3.1.7 on 2021-02-24 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iscrizioni', '0023_evento_istruzioni_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attivita',
            old_name='crediti_riconosciuti',
            new_name='valore_crediti_riconosciuti',
        ),
    ]
