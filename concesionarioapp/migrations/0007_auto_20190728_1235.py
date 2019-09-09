# Generated by Django 2.2.3 on 2019-07-28 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concesionarioapp', '0006_auto_20180305_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datospersonales',
            name='datipoid',
            field=models.CharField(blank=True, choices=[('CC', 'Cédula de Ciudadanía (CC)'), ('TI', 'Tarjeta de Identidad (TI)'), ('RC', 'Registro Civil (RC)'), ('CE', 'Cédula de Extranjería (CE)'), ('CI', 'Carné de Identidad (CI)'), ('DNI', 'Documento Nacional de Identidad (DNI)'), ('DUI', 'Documento Único de Identidad (DUI)')], default='CC', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='datospersonales',
            name='foto',
            field=models.ImageField(default='usuarios/usuario.png', upload_to='usuarios'),
        ),
    ]
