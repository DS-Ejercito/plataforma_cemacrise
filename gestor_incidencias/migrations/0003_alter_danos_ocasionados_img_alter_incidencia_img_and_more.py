# Generated by Django 5.0.2 on 2024-11-27 16:06

import gestor_incidencias.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor_incidencias', '0002_est_dano_tp_asist_tp_dano_alter_incidencia_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='danos_ocasionados',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to=gestor_incidencias.models.camb_nom_arch),
        ),
        migrations.AlterField(
            model_name='incidencia',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to=gestor_incidencias.models.camb_nom_arch),
        ),
        migrations.AlterField(
            model_name='pers_asist',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to=gestor_incidencias.models.camb_nom_arch),
        ),
    ]
