# Generated by Django 4.1.7 on 2023-08-21 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Servicios', '0003_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicio',
            options={'ordering': ['id_servicio']},
        ),
    ]
