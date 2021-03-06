# Generated by Django 2.2.6 on 2019-10-21 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('answerStartTime', models.TimeField()),
                ('answerEndTime', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='InviteControl',
            fields=[
                ('inviteId', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('activated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('inviteId', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('name', models.TextField(help_text='Digite seu nome', max_length=100)),
                ('origin', models.IntegerField(choices=[('I', 'Industry - Professional from industry'), ('M', 'Academics - Professional from academy [student, master or PHD]')])),
                ('experience', models.TextField(choices=[('0-2', '0 to 2 years of experience'), ('3-5', '3 to 5 years of experience'), ('6-8', '6 to 8 years of experience'), ('MT9', 'More than 9 years of experience')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dtStartTasks', models.DateTimeField()),
                ('dtEndTasks', models.DateTimeField()),
                ('participant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='questionnaire.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_text',
        ),
        migrations.AddField(
            model_name='question',
            name='description',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionnaire.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='questionnaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionnaire.Questionnaire'),
        ),
        migrations.AddField(
            model_name='question',
            name='task',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='questionnaire.Task'),
            preserve_default=False,
        ),
    ]
