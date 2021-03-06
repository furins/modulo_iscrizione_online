# Generated by Django 3.1.7 on 2021-02-24 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iscrizioni', '0030_auto_20210224_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attivita',
            name='opzionale',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='modello_form_evento',
            field=models.CharField(choices=[('default', 'Default'), ('con_attivita', 'Con selezione attività')], default='default', max_length=20),
        ),
    ]
