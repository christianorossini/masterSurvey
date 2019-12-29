# Generated by Django 2.2.6 on 2019-12-24 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0055_auto_20191224_1926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='csBackground',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='mlBackground',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='name',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='origin',
        ),
        migrations.AddField(
            model_name='participant',
            name='codeRevision',
            field=models.IntegerField(choices=[('0', 'I do not have any experience'), ('1', 'Very low'), ('2', 'Low'), ('3', 'High'), ('4', 'Very high')], default=0),
        ),
        migrations.AddField(
            model_name='participant',
            name='codeRevision_qtdProjects',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='participant',
            name='codeRevision_qtdProjectsIndustry',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='participant',
            name='codeRevision_qtdYears',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='participant',
            name='codeSmellIdentification',
            field=models.IntegerField(choices=[('0', 'I do not have any experience'), ('1', 'Very low'), ('2', 'Low'), ('3', 'High'), ('4', 'Very high')], default=0),
        ),
        migrations.AddField(
            model_name='participant',
            name='codeSmellIdentification_qtdProjects',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='participant',
            name='codeSmellIdentification_qtdProjectsIndustry',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='participant',
            name='codeSmellIdentification_qtdYears',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='participant',
            name='degree',
            field=models.CharField(default='', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='devExperience',
            field=models.IntegerField(choices=[('0', 'I do not have any experience'), ('1', 'Very low'), ('2', 'Low'), ('3', 'High'), ('4', 'Very high')], default=0),
        ),
        migrations.AddField(
            model_name='participant',
            name='devExperience_qtdProjects',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='participant',
            name='devExperience_qtdProjectsIndustry',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='participant',
            name='devExperience_qtdYears',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='participant',
            name='dsDevelopmentExperience',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='dsIndustryRole',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='javaExperience',
            field=models.IntegerField(choices=[('0', 'I do not have any experience'), ('1', 'Very low'), ('2', 'Low'), ('3', 'High'), ('4', 'Very high')], default=0),
        ),
        migrations.AddField(
            model_name='participant',
            name='javaExperience_qtdProjects',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='participant',
            name='javaExperience_qtdProjectsIndustry',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='participant',
            name='javaExperience_qtdYears',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='participant',
            name='objOrientedExperience',
            field=models.IntegerField(choices=[('0', 'I do not have any experience'), ('1', 'Very low'), ('2', 'Low'), ('3', 'High'), ('4', 'Very high')], default=0),
        ),
        migrations.AddField(
            model_name='participant',
            name='objOrientedExperience_qtdProjects',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='participant',
            name='objOrientedExperience_qtdProjectsIndustry',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='participant',
            name='objOrientedExperience_qtdYears',
            field=models.IntegerField(default=0),
        ),
    ]