from django.db import models

class Participant(models.Model):
    inviteId = models.CharField(primary_key=True,unique=True,max_length=10)
    PART_ORIGIN = (
        ('I', 'Industry - Professional from industry'),
        ('M', 'Academics - Professional from academy [student, master or PHD]'),        
    )
    YEARS_OF_EXP = (
        ('0-2', '0 to 2 years of experience'),
        ('3-5', '3 to 5 years of experience'),
        ('6-8', '6 to 8 years of experience'),
        ('MT9', 'More than 9 years of experience'),        
    )
    name = models.CharField(max_length=100, blank=False, verbose_name="Name (or Nickname)")
    origin = models.CharField(choices=PART_ORIGIN, max_length=1) 
    experience = models.CharField(max_length=3, choices=YEARS_OF_EXP, verbose_name="Programming experience") # experience with code smell study or research 1 to 3 years, 4 to 6 years, 7 or more

    def __str__(self):
        return self.name

class DTModel(models.Model):
    imgPath = models.CharField(max_length=50)
    codeSnippet1 = models.TextField()
    codeSnippert2 = models.TextField()    

class Task(models.Model):
    name = models.CharField(max_length=30, default='')
    dtModel = models.ForeignKey(DTModel, on_delete=models.DO_NOTHING)
    
class Question(models.Model):
    description = models.TextField(max_length=100, default="")
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    sequenceNumber = models.IntegerField() #as 'questions' tem uma sequência dentro de uma task
    
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
    