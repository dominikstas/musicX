# Generated by Django 4.2.5 on 2023-09-24 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plyta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytul', models.CharField(max_length=255)),
                ('wykonawca', models.CharField(max_length=255)),
                ('nosnik', models.CharField(max_length=50)),
            ],
        ),
    ]
