# Generated by Django 4.1.3 on 2022-11-30 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaEvento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PaisDestino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('moneda', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PlataformaStream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Productor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('telefono', models.IntegerField()),
                ('mail', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TipoEvento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
                ('cantidadEntradas', models.IntegerField()),
                ('artistasParticipantes', models.TextField()),
                ('inicioStream', models.DateTimeField()),
                ('finStream', models.DateTimeField()),
                ('fechaConfirmacion', models.DateTimeField()),
                ('fechaRegistro', models.DateTimeField()),
                ('link', models.CharField(max_length=30)),
                ('urlImg', models.CharField(max_length=30)),
                ('idEstado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appStreaming.estado')),
                ('idPais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appStreaming.paisdestino')),
                ('idPlataforma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appStreaming.plataformastream')),
                ('idProductor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appStreaming.productor')),
                ('idTipoEvento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appStreaming.tipoevento')),
            ],
        ),
    ]
