# Generated by Django 4.2.5 on 2023-09-25 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0004_plyta_zdjecie'),
    ]

    operations = [
        migrations.AddField(
            model_name='plyta',
            name='rok_zakupu',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
