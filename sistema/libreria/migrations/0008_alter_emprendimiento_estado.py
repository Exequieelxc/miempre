# Generated by Django 3.2.8 on 2023-11-25 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0007_auto_20231124_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprendimiento',
            name='estado',
            field=models.CharField(choices=[('disponible', 'Disponible'), ('no_disponible', 'No Disponible')], max_length=20),
        ),
    ]
