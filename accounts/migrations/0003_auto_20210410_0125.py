# Generated by Django 3.1.5 on 2021-04-09 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210410_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='height',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nationality',
            field=models.CharField(default='বাংলাদেশী', max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='proffession',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='religion',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='skinTone',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='weight',
            field=models.CharField(default='', max_length=50),
        ),
    ]
