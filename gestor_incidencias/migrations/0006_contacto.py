# Generated by Django 5.0.2 on 2025-03-09 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor_incidencias', '0005_cv'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField(blank=True, null=True, unique=True)),
                ('depto', models.CharField(max_length=100)),
                ('munic', models.CharField(max_length=100)),
                ('cv', models.CharField(max_length=100)),
                ('grado1', models.CharField(max_length=100)),
                ('nom1', models.CharField(max_length=100)),
                ('num1', models.CharField(max_length=100)),
                ('grado2', models.CharField(max_length=100)),
                ('nom2', models.CharField(max_length=100)),
                ('num2', models.CharField(max_length=100)),
            ],
        ),
    ]
