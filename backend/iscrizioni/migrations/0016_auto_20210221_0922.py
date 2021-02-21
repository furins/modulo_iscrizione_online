# Generated by Django 3.1.7 on 2021-02-21 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iscrizioni', '0015_auto_20210220_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='utente',
            name='codice_fiscale',
            field=models.CharField(blank=True, max_length=16),
        ),
        migrations.AlterField(
            model_name='accreditamentoordine',
            name='regione',
            field=models.CharField(blank=True, choices=[('Abruzzo', 'Abruzzo'), ('Basilicata', 'Basilicata'), ('Calabria', 'Calabria'), ('Campania', 'Campania'), ('Emilia-Romagna', 'Emilia Romagna'), ('Friuli-Venezia Giulia', 'Friuli Venezia Giulia'), ('Lazio', 'Lazio'), ('Liguria', 'Liguria'), ('Lombardia', 'Lombardia'), ('Marche', 'Marche'), ('Molise', 'Molise'), ('Piemonte', 'Piemonte'), ('Puglia', 'Puglia'), ('Sardegna', 'Sardegna'), ('Sicilia', 'Sicilia'), ('Toscana', 'Toscana'), ('Trentino-Alto Adige', 'Trentino Alto Adige'), ('Umbria', 'Umbria'), ("Valle d'Aosta", 'Valle D Aosta'), ('Veneto', 'Veneto')], max_length=21, null=True),
        ),
        migrations.AlterField(
            model_name='utente',
            name='provincia',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name='utente',
            name='regione',
            field=models.CharField(blank=True, choices=[('Abruzzo', 'Abruzzo'), ('Basilicata', 'Basilicata'), ('Calabria', 'Calabria'), ('Campania', 'Campania'), ('Emilia-Romagna', 'Emilia Romagna'), ('Friuli-Venezia Giulia', 'Friuli Venezia Giulia'), ('Lazio', 'Lazio'), ('Liguria', 'Liguria'), ('Lombardia', 'Lombardia'), ('Marche', 'Marche'), ('Molise', 'Molise'), ('Piemonte', 'Piemonte'), ('Puglia', 'Puglia'), ('Sardegna', 'Sardegna'), ('Sicilia', 'Sicilia'), ('Toscana', 'Toscana'), ('Trentino-Alto Adige', 'Trentino Alto Adige'), ('Umbria', 'Umbria'), ("Valle d'Aosta", 'Valle D Aosta'), ('Veneto', 'Veneto')], max_length=21, null=True),
        ),
        migrations.DeleteModel(
            name='Regione',
        ),
    ]