# Generated by Django 5.0.3 on 2024-04-27 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agronomie', '0006_remove_endroit_propice_periode_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endroit_propice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_endroit', models.CharField(max_length=50)),
                ('nom_ville', models.CharField(max_length=50)),
                ('description_endroit', models.TextField()),
                ('periode_plantation', models.DateField()),
                ('periode_recolte', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='culture',
            name='endroit_propice',
            field=models.ManyToManyField(to='Agronomie.endroit_propice'),
        ),
    ]