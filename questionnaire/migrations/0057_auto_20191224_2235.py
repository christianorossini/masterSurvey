# Generated by Django 2.2.6 on 2019-12-24 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0056_auto_20191224_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='codeRevision_qtdProjects',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='participant',
            name='codeRevision_qtdProjectsIndustry',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='participant',
            name='codeRevision_qtdYears',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='participant',
            name='codeSmellIdentification_qtdProjects',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='participant',
            name='codeSmellIdentification_qtdProjectsIndustry',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='participant',
            name='codeSmellIdentification_qtdYears',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='participant',
            name='degree',
            field=models.CharField(choices=[('G', 'Bachelor degree'), ('M', 'Master degree'), ('P', 'PHD')], max_length=1),
        ),
        migrations.AlterField(
            model_name='participant',
            name='devExperience_qtdProjects',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='participant',
            name='devExperience_qtdProjectsIndustry',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='participant',
            name='devExperience_qtdYears',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='participant',
            name='javaExperience_qtdProjects',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='participant',
            name='javaExperience_qtdProjectsIndustry',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='participant',
            name='javaExperience_qtdYears',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='participant',
            name='objOrientedExperience_qtdProjects',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='participant',
            name='objOrientedExperience_qtdProjectsIndustry',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='participant',
            name='objOrientedExperience_qtdYears',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
