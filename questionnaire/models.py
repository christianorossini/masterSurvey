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
    OPTIONS_DIFFICULTY = (
            ("VE", "Very easy - I answered without any problems in less then 7 seconds"),
            ("E", "Easy - I found the answer quite quickly and without major problems"),
            ("M", "Medium"),
            ("D","Difficult - I had to think hard and am I am not sure if I answered correctly."),
            ("VD","Very difficult - Despite thinking hard, my answer is likely to be wrong."))    
    secondsToAnswer = models.IntegerField(null=True)    
    questionnaire = models.ForeignKey(Questionnaire,on_delete=models.CASCADE)
    dtModel = models.ForeignKey(DTModel, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    class Meta:
        db_table="ms_answer"  

class AnswerTaskCL(Answer):
    OPTIONSQ1 = (            
            ("CS", "It belongs to class 'Code smell'"),
            ("NC", "It DOESN'T belongs to class 'Code smell'")) 
    """ OPTIONSQ2 = (            
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
            ) """ 
    answerq1 = models.CharField(max_length=2, verbose_name='', choices=OPTIONSQ1)
    answerq2 = models.CharField(max_length=2, verbose_name='', choices=Answer.OPTIONS_DIFFICULTY)
    class Meta:
        db_table="ms_answerTaskCL" 

class InviteControl(models.Model):
    inviteId = models.CharField(primary_key=True,unique=True,max_length=10)
    activated = models.BooleanField(default=False)
    class Meta:
        db_table="ms_inviteControl"
    