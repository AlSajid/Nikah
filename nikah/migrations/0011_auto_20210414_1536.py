# Generated by Django 3.1.3 on 2021-04-14 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nikah', '0010_auto_20210414_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='details',
            field=models.CharField(default=' ', max_length=500),
        ),
    ]
