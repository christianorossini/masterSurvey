# Generated by Django 2.2.6 on 2019-12-07 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0044_auto_20191207_1757'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GroupQueueLog',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='nuGroup',
        ),
    ]
