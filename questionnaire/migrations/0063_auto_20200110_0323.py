# Generated by Django 2.2.6 on 2020-01-10 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0062_auto_20200109_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='codeSnippet2Content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='codeSnippet2URI',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]