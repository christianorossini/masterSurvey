from django.db import models
from datetime import datetime

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
    BG_CS = (
        ('NK', 'Not knowledgeable (I do not know anything)'),
        ('SK', 'Somewhat knowledgeable (I have a vague idea)'),
        ('K', 'Knowledgeable (I am familiar with it)'),
        ('VK', 'Very knowledgeable (I know all/most classes and methods of it)'),        
    )
    BG_ML = (
        ('NK', 'Not knowledgeable (I do not know anything)'),
        ('SK', 'Somewhat knowledgeable (I have a vague idea)'),
        ('K', 'Knowledgeable (I am familiar with it)'),
        ('VK', 'Very knowledgeable (I know all/most classes and methods of it)'),
    )    
    name = models.CharField(max_length=100, blank=False, verbose_name="Name (or Nickname)")
    origin = models.CharField(choices=PART_ORIGIN, max_length=1) 
    experience = models.CharField(max_length=3, choices=YEARS_OF_EXP, verbose_name="Programming experience") # experience with code smell study or research 1 to 3 years, 4 to 6 years, 7 or more
    csBackground = models.CharField(max_length=2, choices=BG_CS, verbose_name="Rate your background/knowledge about Code Smells")
    csdtBackground = models.CharField(max_length=2, choices=BG_CS, verbose_name="Rate your background/knowledge about Code Smells Detection Tools")
    mlBackground = models.CharField(max_length=2, choices=BG_ML, verbose_name="Rate your background/knowledge about machine learning and decision tree")
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

class Task(models.Model):
    CLASSIFY_TASK = "CL"
    RATE_TASK = "RA"
    IDENTIFY_TASK = "ID"
    shortName = models.CharField(max_length=2)
    name = models.CharField(max_length=30, default='')    
    questions = models.ManyToManyField(Question)
    sequenceNumber = models.IntegerField(null=True) #ordem de exibição das tasks
    def __str__(self):
        return self.name
    class Meta:
        db_table="ms_task"      
    def getForm(self, post=None, instance=None):
        from . import forms
        if (self.shortName==Task.CLASSIFY_TASK):
            return forms.AnswerTaskCLForm(post, instance=instance)            
        if (self.shortName==Task.RATE_TASK):    
            return forms.AnswerTaskRAForm(post, instance=instance)            
        if (self.shortName==Task.IDENTIFY_TASK):    
            return forms.AnswerTaskIDForm(post, instance=instance)                
    def getView(self):
        if (self.shortName==Task.CLASSIFY_TASK):            
            return "masterquest/survey_task_cl.html"
        if (self.shortName==Task.RATE_TASK):                
            return "masterquest/survey_task_ra.html"
        if (self.shortName==Task.IDENTIFY_TASK):                
            return "masterquest/survey_task_id.html"    

class DTModel(models.Model):
    imgPath = models.CharField(max_length=50)
    modelTreePath = models.CharField(max_length=200, null=True)
    codeSnippet1 = models.TextField()
    codeSnippet2 = models.TextField()    
    tasks = models.ManyToManyField(Task)
    sequenceNumber = models.IntegerField(null=True) #ordem de exibição dos modelos de DT
    def __str__(self):
        return self.imgPath
    class Meta:
        db_table="ms_dtModel"        

class Questionnaire(models.Model):
    participant = models.OneToOneField(Participant, on_delete=models.CASCADE)
    dtStartTasks = models.DateTimeField(auto_now_add=True)
    dtEndTasks = models.DateTimeField(null=True)    
    class Meta:
        db_table="ms_questionnaire"   
    def __str__(self):
        return str(self.dtStartTasks)
    def finish(self):
        self.dtEndTasks = datetime.now()

class Answer(models.Model):    
    OPTIONS_DIFFICULTY = (
            ("VE", "Very easy - I answered without any problems in less then 7 seconds"),
            ("E", "Easy - I found the answer quite quickly and without major problems"),
            ("M", "Medium"),
            ("D","Difficult - I had to think hard and am I am not sure if I answered correctly."),
            ("VD","Very difficult - Despite thinking hard, my answer is likely to be wrong."))    
    secondsToAnswer = models.FloatField(null=True)    
    questionnaire = models.ForeignKey(Questionnaire,on_delete=models.CASCADE)
    dtModel = models.ForeignKey(DTModel, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    class Meta:
        db_table="ms_answer"  

# Classe para respostas da task Classification
class AnswerTaskCL(Answer):
    OPTIONS_CLASSIFY = (            
            ("CS", "It belongs to class 'Code smell'"),
            ("NC", "It DOESN'T belongs to class 'Code smell'"))    
    answerq1 = models.CharField(max_length=2, verbose_name='', choices=OPTIONS_CLASSIFY)
    answerq2 = models.CharField(max_length=2, verbose_name='', choices=Answer.OPTIONS_DIFFICULTY)
    class Meta:
        db_table="ms_answerTaskCL" 

# Classe para respostas da task Identify
class AnswerTaskID(Answer):    
    OPTIONS_CODE_SMELL = (            
            ("CDSBP", "Class Data Should Be Private"),
            ("CC", "Complex Class"),
            ("FE", "Feature Envy"),
            ("GC", "God Class"),
            ("II", "Inappropriate Intimacy"),
            ("LC", "Lazy Class"),
            ("LM", "Long Method"),
            ("LPL", "Long Parameter List"),
            ("MM", "Middle Man"),
            ("RB", "Refused Bequest"),
            ("SC", "Spaghetti Code"),
            ("SG", "Speculative Generality"),
            )
    answerq1 = models.CharField(max_length=5, verbose_name='', choices=OPTIONS_CODE_SMELL)    
    class Meta:
        db_table="ms_answerTaskID"

# Classe para respostas da task Rate
class AnswerTaskRA(Answer):    
    OPTIONS_RATE = (            
            ("VE", "Very easily comprehensible"),
            ("E", "Easily comprehensible"),
            ("C", "Comprehensible"),
            ("D", "Difficult to comprehend"),
            ("VD", "Very difficult to comprehend"),
            )
    answerq1 = models.CharField(max_length=2, verbose_name='', choices=OPTIONS_RATE, default='')    
    class Meta:
        db_table="ms_answerTaskRA"

class InviteControl(models.Model):
    inviteId = models.CharField(primary_key=True,unique=True,max_length=10)
    activated = models.BooleanField(default=False)
    class Meta:
        db_table="ms_inviteControl"
    