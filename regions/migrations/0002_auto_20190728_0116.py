# Generated by Django 2.2.3 on 2019-07-28 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commune',
            name='commune_name',
            field=models.CharField(max_length=100),
        ),
    ]
