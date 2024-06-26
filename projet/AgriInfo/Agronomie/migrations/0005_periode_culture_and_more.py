# Generated by Django 5.0.3 on 2024-04-27 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agronomie', '0004_remove_endroit_propice_culture_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Periode_culture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periode_plantation', models.DateField()),
                ('periode_recolte', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='endroit_propice',
            name='periode_plantation',
        ),
        migrations.RemoveField(
            model_name='endroit_propice',
            name='periode_recolte',
        ),
        migrations.AddField(
            model_name='endroit_propice',
            name='periode',
            field=models.ManyToManyField(to='Agronomie.periode_culture'),
        ),
    ]
