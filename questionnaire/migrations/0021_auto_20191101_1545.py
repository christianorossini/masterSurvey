# Generated by Django 2.2.6 on 2019-11-01 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0020_auto_20191101_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='dtmodel',
            name='modelTreePath',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='answertaskid',
            name='answerq1',
            field=models.CharField(choices=[('CDSBP', 'Class Data Should Be Private'), ('CC', 'Complex Class'), ('FE', 'Feature Envy'), ('GC', 'God Class'), ('II', 'Inappropriate Intimacy'), ('LC', 'Lazy Class'), ('LM', 'Long Method'), ('LPL', 'Long Parameter List'), ('MM', 'Middle Man'), ('RB', 'Refused Bequest'), ('SC', 'Spaghetti Code'), ('SG', 'Speculative Generality')], max_length=2, verbose_name=''),
        ),
    ]
