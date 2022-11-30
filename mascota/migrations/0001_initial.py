# Generated by Django 4.1.3 on 2022-11-23 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tipo', models.CharField(choices=[('g', 'Gato'), ('p', 'Perro')], max_length=2)),
                ('sexo', models.CharField(choices=[('h', 'Hembra'), ('m', 'Macho')], max_length=2)),
                ('fecha_nacimiento', models.DateField()),
                ('tamano_final', models.CharField(choices=[('p', 'Pequeño'), ('m', 'Mediano'), ('g', 'Grande')], max_length=2)),
                ('responsable', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('ubicacion', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('desparasitado', models.BooleanField()),
                ('vacunado', models.BooleanField()),
                ('castrado', models.BooleanField()),
            ],
        ),
    ]
