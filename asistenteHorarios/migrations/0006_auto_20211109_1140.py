# Generated by Django 3.2.3 on 2021-11-09 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asistenteHorarios', '0005_horario_instructor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contratacion',
            name='Fecha_Fin',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='contratacion',
            name='Fecha_Inicio',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='horario_instructor',
            name='Fecha_Fin',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='horario_instructor',
            name='Fecha_Inicio',
            field=models.DateTimeField(),
        ),
    ]
