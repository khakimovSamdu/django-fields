# Generated by Django 5.0.2 on 2024-02-20 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_it_markaz_date_auto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='it_markaz',
            name='date_auto',
            field=models.DateField(auto_now=True),
        ),
    ]
