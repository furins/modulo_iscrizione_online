# Generated by Django 3.1.7 on 2021-02-21 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iscrizioni', '0018_auto_20210221_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accreditamentoordine',
            name='ordine',
            field=models.CharField(choices=[('Consiglio nazionale ingegneri', 'Ingegneri'), ('Consiglio nazionale architetti, pianificatori, paesaggisti e conservatori', 'Architetti'), ('Consiglio nazionale dei chimici', 'Chimici'), ('Consiglio nazionale dei geologi', 'Geologi'), ('Ordine nazionale dei biologi', 'Biologi'), ('Ordine nazionale dei dottori agronomi e dottori forestali', 'Agronomi')], max_length=73),
        ),
        migrations.AlterField(
            model_name='accreditamentoordine',
            name='regione',
            field=models.CharField(choices=[('Abruzzo', 'Abruzzo'), ('Basilicata', 'Basilicata'), ('Calabria', 'Calabria'), ('Campania', 'Campania'), ('Emilia-Romagna', 'Emilia Romagna'), ('Friuli-Venezia Giulia', 'Friuli Venezia Giulia'), ('Lazio', 'Lazio'), ('Liguria', 'Liguria'), ('Lombardia', 'Lombardia'), ('Marche', 'Marche'), ('Molise', 'Molise'), ('Piemonte', 'Piemonte'), ('Puglia', 'Puglia'), ('Sardegna', 'Sardegna'), ('Sicilia', 'Sicilia'), ('Toscana', 'Toscana'), ('Trentino-Alto Adige', 'Trentino Alto Adige'), ('Umbria', 'Umbria'), ("Valle d'Aosta", 'Valle D Aosta'), ('Veneto', 'Veneto')], default='Veneto', max_length=21),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='utente',
            name='ordine_di_appartenenza',
            field=models.CharField(blank=True, choices=[('Consiglio nazionale ingegneri', 'Ingegneri'), ('Consiglio nazionale architetti, pianificatori, paesaggisti e conservatori', 'Architetti'), ('Consiglio nazionale dei chimici', 'Chimici'), ('Consiglio nazionale dei geologi', 'Geologi'), ('Ordine nazionale dei biologi', 'Biologi'), ('Ordine nazionale dei dottori agronomi e dottori forestali', 'Agronomi')], max_length=73, null=True),
        ),
        migrations.DeleteModel(
            name='Ordine',
        ),
    ]
