# Generated by Django 3.2.3 on 2021-11-21 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asistenteHorarios', '0010_resultados'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdenRAP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrdenRap', models.IntegerField()),
                ('Ficha', models.ManyToManyField(to='asistenteHorarios.FichasCaracterizacion')),
                ('Resultado', models.ManyToManyField(to='asistenteHorarios.Resultados')),
            ],
        ),
    ]
