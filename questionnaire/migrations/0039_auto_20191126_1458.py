# Generated by Django 2.2.6 on 2019-11-26 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0038_auto_20191125_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='csdtBackground',
        ),
        migrations.AlterField(
            model_name='participant',
            name='csBackground',
            field=models.CharField(choices=[('NK', 'Not knowledgeable (I do not know anything)'), ('SK', 'Somewhat knowledgeable (I have a vague idea)'), ('K', 'Knowledgeable (I am familiar with it)'), ('VK', 'Very knowledgeable (I know all about it)')], max_length=2, verbose_name='Rate your background/knowledge about Code Smells'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='mlBackground',
            field=models.CharField(choices=[('NK', 'Not knowledgeable (I do not know anything)'), ('SK', 'Somewhat knowledgeable (I have a vague idea)'), ('K', 'Knowledgeable (I am familiar with it)'), ('VK', 'Very knowledgeable (I know all about ir)')], max_length=2, verbose_name='Rate your background/knowledge about machine learning and decision tree'),
        ),
    ]