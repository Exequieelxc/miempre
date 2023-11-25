# Generated by Django 3.2.8 on 2023-11-25 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0006_auto_20231121_0234'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emprendimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(upload_to='emprendimientos/')),
                ('estado', models.CharField(choices=[('disponible', 'Disponible'), ('no_disponible', 'No Disponible')], max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='Biblioteca',
        ),
        migrations.DeleteModel(
            name='Libro',
        ),
        migrations.DeleteModel(
            name='Proveedor',
        ),
    ]
