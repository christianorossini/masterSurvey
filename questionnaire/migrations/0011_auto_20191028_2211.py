# Generated by Django 2.2.6 on 2019-10-28 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0010_task_shortname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dtmodel',
            old_name='codeSnippert2',
            new_name='codeSnippet2',
        ),
        migrations.AlterField(
            model_name='answer',
            name='content',
            field=models.CharField(max_length=5, verbose_name=''),
        ),
    ]
