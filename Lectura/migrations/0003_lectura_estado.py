# Generated by Django 4.1 on 2023-09-08 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lectura', '0002_alter_lectura_mes'),
    ]

    operations = [
        migrations.AddField(
            model_name='lectura',
            name='estado',
            field=models.IntegerField(default=0),
        ),
    ]
