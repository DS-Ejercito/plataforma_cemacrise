# Generated by Django 4.2.7 on 2024-11-18 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='depto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descrip_corta', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='tp_incidencia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descrip_corta', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='procedencia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descrip_corta', models.TextField()),
                ('descrip_larga', models.TextField()),
                ('cod_proced_superior', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategorias', to='gestor_incidencias.procedencia')),
            ],
        ),
        migrations.CreateModel(
            name='munic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descrip_corta', models.TextField()),
                ('cod_depto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategorias', to='gestor_incidencias.munic')),
            ],
        ),
        migrations.CreateModel(
            name='incidencia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('obser', models.TextField(blank=True, null=True)),
                ('longitud', models.FloatField(null=True)),
                ('latitud', models.FloatField(null=True)),
                ('cant', models.FloatField(null=True)),
                ('img', models.FileField(blank=True, null=True, upload_to='Incidencias/')),
                ('depto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestor_incidencias.depto')),
                ('munic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestor_incidencias.munic')),
                ('procedencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestor_incidencias.procedencia')),
                ('tp_incidencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestor_incidencias.tp_incidencia')),
            ],
        ),
    ]