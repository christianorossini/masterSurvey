# Generated by Django 2.2.6 on 2019-10-22 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0002_auto_20191021_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='experience',
            field=models.CharField(choices=[('0-2', '0 to 2 years of experience'), ('3-5', '3 to 5 years of experience'), ('6-8', '6 to 8 years of experience'), ('MT9', 'More than 9 years of experience')], max_length=3),
        ),
        migrations.AlterField(
            model_name='participant',
            name='name',
            field=models.CharField(help_text='Name', max_length=100),
        ),
    ]
