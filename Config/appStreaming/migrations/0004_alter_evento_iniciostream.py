# Generated by Django 4.1.4 on 2022-12-20 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appStreaming', '0003_alter_evento_iniciostream'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='inicioStream',
            field=models.DateTimeField(),
        ),
    ]
