# Generated by Django 2.2.6 on 2019-11-25 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0036_auto_20191125_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dtmodel',
            name='dtDepth',
            field=models.IntegerField(null=True),
        ),
    ]