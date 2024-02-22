# Generated by Django 5.0.2 on 2024-02-21 21:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_samdu_float_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='samdu',
            name='file_field',
            field=models.FileField(default=django.utils.timezone.now, upload_to='uploads/'),
            preserve_default=False,
        ),
    ]
