# Generated by Django 2.2.4 on 2019-11-07 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0012_auto_20191107_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='imagen',
            field=models.ImageField(default=0, upload_to='mascotas'),
            preserve_default=False,
        ),
    ]
