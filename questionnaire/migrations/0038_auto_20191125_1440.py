# Generated by Django 2.2.6 on 2019-11-25 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0037_auto_20191125_1434'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dtmodel',
            old_name='codePSnippetProject',
            new_name='codeSnippetProject',
        ),
        migrations.AddField(
            model_name='dtmodel',
            name='codeSmellType',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
