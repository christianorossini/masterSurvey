# Generated by Django 2.2.6 on 2020-01-10 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0063_auto_20200110_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answertaskid',
            name='answer_csagreement',
            field=models.IntegerField(choices=[(2, 'Agree Strongly'), (1, 'Agree Slightly'), (-1, 'Disagree Slightly'), (-2, 'Disagree Strongly')], default=None),
        ),
    ]
