# Generated by Django 4.2.7 on 2025-05-03 14:10

from django.db import migrations, models
import django.db.models.deletion
import gestor_incidencias.models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor_incidencias', '0007_munic_cod_munic'),
    ]

    operations = [
        migrations.CreateModel(
            name='area',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descrip_corta', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='contactoxcv',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('num', models.CharField(max_length=100)),
                ('img', models.FileField(blank=True, null=True, upload_to=gestor_incidencias.models.camb_nom_arch)),
            ],
        ),
        migrations.AddField(
            model_name='cv',
            name='carga_electoral',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='cv',
            name='sector_electoral',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cv',
            name='cod_area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestor_incidencias.area'),
        ),
    ]
