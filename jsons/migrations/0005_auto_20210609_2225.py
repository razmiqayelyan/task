# Generated by Django 3.1.7 on 2021-06-09 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jsons', '0004_auto_20210609_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giftshop',
            name='citizen_id',
            field=models.IntegerField(default=973),
        ),
    ]
