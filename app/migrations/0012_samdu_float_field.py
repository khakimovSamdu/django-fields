# Generated by Django 5.0.2 on 2024-02-21 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_remove_samdu_float_field_'),
    ]

    operations = [
        migrations.AddField(
            model_name='samdu',
            name='float_field',
            field=models.FloatField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]