# Generated by Django 3.1.4 on 2021-08-18 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_auto_20210818_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messageinsert',
            name='nameInsert',
            field=models.CharField(max_length=100),
        ),
    ]
