# Generated by Django 3.1.7 on 2021-02-20 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iscrizioni', '0004_auto_20210220_1713'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='iscrizione',
            options={'ordering': ['iscritto__cognome', 'iscritto__nome'], 'verbose_name_plural': 'Iscrizioni'},
        ),
        migrations.AlterModelOptions(
            name='utente',
            options={'ordering': ['cognome', 'nome'], 'verbose_name_plural': 'Utenti'},
        ),
    ]
