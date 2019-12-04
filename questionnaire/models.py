from django.db import models
from datetime import datetime
import secrets

class GroupQueueLog(models.Model):
    OPTIONS_GROUP = ((1,"Group 1"),(2,"Group 2"))
    dtInsertion = models.DateTimeField(auto_now_add=True)
    nuGroup = models.IntegerField(choices=OPTIONS_GROUP)
    class Meta:
        db_table="ms_groupQueueLog"

class Participant(models.Model):        
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
        ('VK', 'Very knowledgeable (I know all about it)'),        
    )
    BG_ML = (
        ('NK', 'Not knowledgeable (I do not know anything)'),
        ('SK', 'Somewhat knowledgeable (I have a vague idea)'),
        ('K', 'Knowledgeable (I am familiar with it)'),
        ('VK', 'Very knowledgeable (I know all about ir)'),
    )    
    inviteId = models.CharField(primary_key=True,unique=True,max_length=10)
    nuGroup = models.IntegerField(choices=GroupQueueLog.OPTIONS_GROUP) 
    name = models.CharField(max_length=100, blank=False, verbose_name="Name (or Nickname)")
    origin = models.CharField(choices=PART_ORIGIN, max_length=1) 
    experience = models.CharField(max_length=3, choices=YEARS_OF_EXP, verbose_name="Programming experience") # experience with code smell study or research 1 to 3 years, 4 to 6 years, 7 or more
    csBackground = models.CharField(max_length=2, choices=BG_CS, verbose_name="Rate your background/knowledge about Code Smells")    
    mlBackground = models.CharField(max_length=2, choices=BG_ML, verbose_name="Rate your background/knowledge about machine learning and decision tree")
    
    def save(self):
        self.inviteId = secrets.token_hex(5) #atribuição manual do inviteId, enquanto se estuda o uso do atributo
        # TODO setar um grupo para o usuário.
        super().save()
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table="ms_participant"

    

class Task(models.Model):    
    RATE_TASK = "RA"
    IDENTIFY_TASK = "ID"
    CORRELATION_TASK = "CC"
    shortName = models.CharField(max_length=2)
    name = models.CharField(max_length=30, default='')        
    sequenceNumber = models.IntegerField(null=True) #ordem de exibição das tasks
    def __str__(self):
        return self.name
    class Meta:
        db_table="ms_task"      
    def getForm(self, post=None, instance=None):
        from . import forms                
        if (self.shortName==Task.IDENTIFY_TASK):    
            return forms.AnswerTaskIDForm(post, instance=instance)
        if (self.shortName==Task.CORRELATION_TASK):
            return forms.AnswerTaskCCForm(post, instance=instance)
    def getView(self):                
        if (self.shortName==Task.IDENTIFY_TASK):                
            return "masterquest/survey_task_id.html"    
        if (self.shortName==Task.CORRELATION_TASK):
            return "masterquest/survey_task_cc.html"

class DTModel(models.Model):
    dtImg = models.CharField(max_length=50)    
    dtNumberOfLeaves = models.IntegerField()
    dtDepth = models.IntegerField(null=True)        
    codeSmellType = models.CharField(max_length=10)
    codeSnippetProject = models.CharField(max_length=100)
    codeSnippetKind = models.CharField(max_length=30)
    codeSnippetURI = models.CharField(max_length=200)
    codeSnippet = models.TextField()    
    tasks = models.ManyToManyField(Task)    
    def __str__(self):
        return self.dtImg
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
    OPTIONS_CODE_CONFIDENCE = (
            (4, "Very confident"),
            (3, "Confident"),
            (2, "A little bit confident"),
            (1,"Not confident at all"),            
            ) 
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
    questionnaire = models.ForeignKey(Questionnaire,on_delete=models.CASCADE)
    dtModel = models.ForeignKey(DTModel, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    class Meta:
        db_table="ms_answer"  

# Classe para respostas da task Identify
class AnswerTaskID(Answer):           
    answer_cst = models.CharField(max_length=5, choices=Answer.OPTIONS_CODE_SMELL)    
    answer_cst_confidence = models.IntegerField(verbose_name='', choices=Answer.OPTIONS_CODE_CONFIDENCE, default=None)
    class Meta:
        db_table="ms_answerTaskID"

# Classe para respostas da task Code Correlations
class AnswerTaskCC(Answer):                
    OPTIONS_TREE_RATE = (            
            (5, "Very easily comprehensible"),
            (4, "Easily comprehensible"),
            (3, "Comprehensible"),
            (2, "Difficult to comprehend"),
            (1, "Very difficult to comprehend"),
            )
    OPTIONS_TREE_INFLUENCED_DECISION = (                        
            (3, "Very much"),
            (2, "Not so much"),
            (1, "None"),
            )
    # escolha da decision tree
    answer_cst = models.CharField(max_length=5, verbose_name='', choices=Answer.OPTIONS_CODE_SMELL)    
    # escolha da 'confidence' da opção anterior
    answer_cst_confidence = models.IntegerField(verbose_name='', choices=Answer.OPTIONS_CODE_CONFIDENCE, default=None)
    # escolha do quanto a DT influenciou na tomada de decisão
    answer_cst_dm = models.IntegerField(verbose_name='', choices=OPTIONS_TREE_INFLUENCED_DECISION, default=None)
    # escolha do quanto a DT é compreensível 
    answer_tr = models.IntegerField(verbose_name='', choices=OPTIONS_TREE_RATE, default=None)    
    # texto aberto sobre a opção feita anteriormente
    answer_tr_complement = models.TextField(verbose_name='')    

    class Meta:
        db_table="ms_answerTaskCC"

class InviteControl(models.Model):
    inviteId = models.CharField(primary_key=True,unique=True,max_length=10)
    activated = models.BooleanField(default=False)
    class Meta:
        db_table="ms_inviteControl"
  