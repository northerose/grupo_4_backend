# Generated by Django 4.1.3 on 2022-11-27 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='foto',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
