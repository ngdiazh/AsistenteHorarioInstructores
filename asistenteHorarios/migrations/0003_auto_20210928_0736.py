# Generated by Django 3.2.6 on 2021-09-28 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asistenteHorarios', '0002_auto_20210928_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contratacion',
            name='id_Instructor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='asistenteHorarios.instructores'),
        ),
        migrations.AlterField(
            model_name='instructores',
            name='id_Perfiles',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='asistenteHorarios.catalogo_perfiles'),
        ),
        migrations.AlterField(
            model_name='instructores',
            name='id_TipoDocumento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='asistenteHorarios.catalogo_tipodocumento'),
        ),
    ]
