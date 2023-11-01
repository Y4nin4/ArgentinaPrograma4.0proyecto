# Generated by Django 4.2.6 on 2023-11-01 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_pregunta', models.CharField(max_length=200)),
                ('fecha_publicacion', models.DateTimeField(verbose_name='Fecha publicada')),
            ],
        ),
        migrations.CreateModel(
            name='Opcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_opcion', models.CharField(max_length=200)),
                ('cantidad', models.IntegerField(default=0)),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encuestasmascotas.pregunta')),
            ],
        ),
    ]
