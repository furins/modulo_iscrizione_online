# Generated by Django 3.1.7 on 2021-02-20 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iscrizioni', '0014_auto_20210220_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='modello_form_evento',
            field=models.CharField(choices=[('default', 'Default')], default='default', max_length=20),
        ),
    ]
