from django.db import models

class Participant(models.Model):
    inviteId = models.CharField(primary_key=True,unique=True,max_length=10)
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
    origin = models.IntegerField(choices=PART_ORIGIN) 
    experience = models.TextField(max_length=3, choices=YEARS_OF_EXP) # experience with code smell study or research 1 to 3 years, 4 to 6 years, 7 or more

class Task(models.Model):
    name = models.CharField(max_length=30)
    
class Question(models.Model):
    description = models.TextField(max_length=100)
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.question_text

class Questionnaire(models.Model):
    participant = models.OneToOneField(Participant, on_delete=models.CASCADE)
    dtStartTasks = models.DateTimeField()
    dtEndTasks = models.DateTimeField()

class Answer(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    questionnaire = models.ForeignKey(Questionnaire,on_delete=models.CASCADE)    
    answerStartTime = models.TimeField()
    answerEndTime = models.TimeField()
   

class InviteControl(models.Model):
    inviteId = models.CharField(primary_key=True,unique=True,max_length=10)
    activated = models.BooleanField(default=False)