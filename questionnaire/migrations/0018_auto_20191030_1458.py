# Generated by Django 2.2.6 on 2019-10-30 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0017_task_sequencenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answertaskra',
            name='answerq1',
            field=models.CharField(choices=[('VE', 'Very easily comprehensible'), ('E', 'Easily comprehensible'), ('C', 'Comprehensible'), ('D', 'Difficult to comprehend'), ('VD', 'Very difficult to comprehend')], default='', max_length=2, verbose_name=''),
        ),
    ]
