from django.db import models

class Questionnaire(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Participant(models.Model):
    id = models.IntegerField()
    type = models.CharField(max_length=1)
