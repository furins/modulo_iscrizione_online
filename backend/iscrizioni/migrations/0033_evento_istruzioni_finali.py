# Generated by Django 3.1.7 on 2021-02-24 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iscrizioni', '0032_attivita_ordine'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='istruzioni_finali',
            field=models.TextField(blank=True, help_text='Inserire un testo che apparirà alla fine del form di iscrizione (opzionale)'),
        ),
    ]
