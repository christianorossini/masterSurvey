# Generated by Django 2.2.6 on 2019-12-09 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0047_answer_secondstoanswer'),
    ]

    operations = [
        migrations.AddField(
            model_name='dtmodel',
            name='dtNodes',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
