# Generated by Django 4.2.5 on 2023-09-25 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_remove_plyta_wykonawca_alter_plyta_nosnik_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='plyta',
            name='artysta',
            field=models.CharField(default='none', max_length=100),
            preserve_default=False,
        ),
    ]
