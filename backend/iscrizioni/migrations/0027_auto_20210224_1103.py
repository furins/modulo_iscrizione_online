# Generated by Django 3.1.7 on 2021-02-24 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iscrizioni', '0026_auto_20210224_1059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='partecipazioneattivita',
            old_name='data_partecipazione',
            new_name='data_iscrizione',
        ),
    ]