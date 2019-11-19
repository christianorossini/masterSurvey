# Generated by Django 2.2.6 on 2019-11-07 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0025_auto_20191107_0339'),
    ]

    operations = [
        migrations.AddField(
            model_name='answertaskid',
            name='answerq2',
            field=models.CharField(choices=[('HC', 'Highly Correlated - I detected a code smell in the showed code that matches the rules contained in the Decision Tree.'), ('LC', "Low Correlation -  I a detected a code smell in the showed code but I'm not sure wether the code smell type I've detected is the same code smell pointed in decision tree model."), ('NC', "I'ts not correlated / There isn't any correlation.")], default='', max_length=2, verbose_name=''),
        ),
        migrations.AddField(
            model_name='answertaskid',
            name='answerq3',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='answertaskid',
            name='answerq4',
            field=models.CharField(choices=[('HC', 'Highly Correlated - I detected a code smell in the showed code that matches the rules contained in the Decision Tree.'), ('LC', "Low Correlation -  I a detected a code smell in the showed code but I'm not sure wether the code smell type I've detected is the same code smell pointed in decision tree model."), ('NC', "I'ts not correlated / There isn't any correlation.")], default='', max_length=2, verbose_name=''),
        ),
        migrations.AddField(
            model_name='answertaskid',
            name='answerq5',
            field=models.TextField(null=True),
        ),
    ]