# Generated by Django 4.1.3 on 2022-11-29 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0002_mascota_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='provincia',
            field=models.CharField(choices=[('bsas', 'Ciudad Autónoma de Buenos Aires'), ('catamarca', 'Catamarca'), ('chaco', 'Chaco'), ('chubut', 'Chubut'), ('cdba', 'Córdoba'), ('corrientes', 'Corrientes'), ('rios', 'Entre Ríos'), ('formosa', 'Formosa'), ('jujuy', 'Jujuy'), ('pampa', 'La Pampa'), ('rioja', 'La Rioja'), ('mendoza', 'Mendoza'), ('misiones', 'Misiones'), ('neuquen', 'Neuquen'), ('negro', 'Río Negro'), ('salta', 'Salta'), ('juan', 'San Juan'), ('luis', 'San Luis'), ('cruz', 'Santa Cruz'), ('fe', 'Santa Fé'), ('santiago', 'Santiago del Estero'), ('fuego', 'Tierra del Fuego'), ('tucuman', 'Tucumán')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='foto',
            field=models.ImageField(null=True, upload_to='imagenes'),
        ),
    ]
