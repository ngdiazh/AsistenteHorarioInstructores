# Generated by Django 3.2.3 on 2021-11-23 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asistenteHorarios', '0012_competencias_codigocompetencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultados',
            name='Ficha',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='asistenteHorarios.fichascaracterizacion'),
        ),
    ]
