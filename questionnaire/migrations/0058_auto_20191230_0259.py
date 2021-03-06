# Generated by Django 2.2.6 on 2019-12-30 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0057_auto_20191224_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='codeRevision',
            field=models.IntegerField(choices=[(0, 'I do not have any experience'), (1, 'Very low'), (2, 'Low'), (3, 'High'), (4, 'Very high')]),
        ),
        migrations.AlterField(
            model_name='participant',
            name='codeSmellIdentification',
            field=models.IntegerField(choices=[(0, 'I do not have any experience'), (1, 'Very low'), (2, 'Low'), (3, 'High'), (4, 'Very high')]),
        ),
        migrations.AlterField(
            model_name='participant',
            name='devExperience',
            field=models.IntegerField(choices=[(0, 'I do not have any experience'), (1, 'Very low'), (2, 'Low'), (3, 'High'), (4, 'Very high')]),
        ),
        migrations.AlterField(
            model_name='participant',
            name='javaExperience',
            field=models.IntegerField(choices=[(0, 'I do not have any experience'), (1, 'Very low'), (2, 'Low'), (3, 'High'), (4, 'Very high')]),
        ),
        migrations.AlterField(
            model_name='participant',
            name='objOrientedExperience',
            field=models.IntegerField(choices=[(0, 'I do not have any experience'), (1, 'Very low'), (2, 'Low'), (3, 'High'), (4, 'Very high')]),
        ),
    ]
