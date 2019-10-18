from django.db import models

class Task(models.Model):
    name = models.CharField()
    
class Question(models.Model):
    description = models.TextField()
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    task = models.
    
    def __str__(self):
        return self.question_text

class Questionnaire(models.Model):
    participant = models.OneToOneField(Participant, on_delete=models.CASCADE)
    dtStartTasks = models.DateTimeField()
    dtEndTasks = models.DateTimeField()
    
class Participant(models.Model):
    PART_ORIGIN = (
        ('I', 'Industry - Professional from industry'),
        ('M', 'Academics - Professional from academy [student, master or PHD]'),        
    )
    YEARS_OF_EXP = (
        ('0-3', '0 to 3 years of experience'),
        ('4-7', '4 to 7 years of experience'),
        ('MT7', 'More than 7 years of experience'),        
    )
    name = models.TextField(max_length=100, blank=False,help_text="Digite seu nome")
    origin = models.IntegerField(max_length=1, choices=PART_TYPE) 
    experience = models.TextField(max_length=3, choices=YEARS_OF_EXP) # experience with code smell study or research 1 to 3 years, 4 to 6 years, 7 or more
