# Generated by Django 4.2.6 on 2024-09-30 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='qr',
            field=models.ImageField(default='fotos/no_disponible.jpg', upload_to='qr'),
        ),
    ]
