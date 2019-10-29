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
    class Meta:
        db_table="ms_participant"


class Question(models.Model):
    description = models.CharField(max_length=100)    
    sequenceNumber = models.IntegerField() #as 'questions' tem uma sequência dentro de uma task    
    def __str__(self):
        return self.description
    class Meta:
        db_table="ms_question"    
        ordering = ['sequenceNumber']
    def getForm(self):
        from . import forms
        if self.id==5:
            return forms.AnswerFormCL1()
        if self.id==6:
            return forms.AnswerFormCL2()
        if self.id==7:
            return forms.AnswerFormCL3()       

class Task(models.Model):
    CLASSIFICATION_TASK = "CL"
    shortName = models.CharField(max_length=2,unique=True)
    name = models.CharField(max_length=30, default='')    
    questions = models.ManyToManyField(Question)
    def __str__(self):
        return self.name
    class Meta:
        db_table="ms_task"    

class DTModel(models.Model):
    imgPath = models.CharField(max_length=50)
    codeSnippet1 = models.TextField()
    codeSnippet2 = models.TextField()    
    tasks = models.ManyToManyField(Task)
    def __str__(self):
        return self.imgPath
    class Meta:
        db_table="ms_dtModel"    

class Questionnaire(models.Model):
    participant = models.OneToOneField(Participant, on_delete=models.CASCADE)
    dtStartTasks = models.DateTimeField()
    dtEndTasks = models.DateTimeField()
    def __str__(self):
        return self.participant
    class Meta:
        db_table="ms_questionnaire"

class Answer(models.Model):
    content = models.CharField(max_length=5, verbose_name='')
    answerStartTime = models.TimeField()
    answerEndTime = models.TimeField() 
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    questionnaire = models.ForeignKey(Questionnaire,on_delete=models.CASCADE)
    dtModel = models.ForeignKey(DTModel, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    class Meta:
        db_table="ms_answer"    

class InviteControl(models.Model):
    inviteId = models.CharField(primary_key=True,unique=True,max_length=10)
    activated = models.BooleanField(default=False)
    class Meta:
        db_table="ms_inviteControl"
    