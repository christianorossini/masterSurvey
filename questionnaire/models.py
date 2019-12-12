import logging
import os
import random
import secrets
from datetime import datetime

import pandas as pd
from django.db import models


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
    name = models.CharField(max_length=100, blank=False, verbose_name="Name (or Nickname)")
    origin = models.CharField(choices=PART_ORIGIN, max_length=1) 
    experience = models.CharField(max_length=3, choices=YEARS_OF_EXP, verbose_name="Programming experience") # experience with code smell study or research 1 to 3 years, 4 to 6 years, 7 or more
    csBackground = models.CharField(max_length=2, choices=BG_CS, verbose_name="Rate your background/knowledge about Code Smells")    
    mlBackground = models.CharField(max_length=2, choices=BG_ML, verbose_name="Rate your background/knowledge about machine learning and decision tree")
    
    def save(self):
        self.inviteId = secrets.token_hex(5) #atribuição manual do inviteId, enquanto se estuda o uso do atributo        
        super().save()
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table="ms_participant"

    
class LatinSquare(models.Model):    
    cells = [[True, False],     #   DT      |   noDT
            [False, True]]      #   noDT    |   DT
    row1Participant = models.OneToOneField(Participant, on_delete=models.CASCADE, related_name='participant1', null="True")     
    row2Participant = models.OneToOneField(Participant, on_delete=models.CASCADE, related_name='participant2', null="True") 
    column1Tasks = models.CharField(max_length=50)
    column2Tasks = models.CharField(max_length=50)

    # inicializa a instância de latin square
    #     - cria a sequência de atividades por coluna
    #     - atribui o usuário a uma 'row' do latin square
    def init(self, participant):
        self.column1Tasks = self.initColumn(1)
        self.column2Tasks = self.initColumn(2)
        # confere se há o mesmo número de tarefas por coluna: essencial para a execução so survey
        if(len(self.column1Tasks.split(','))!=len(self.column2Tasks.split(','))):     
            msg = 'Latin Square Columns with diferent number of tasks.'
            logging.warning(msg)
            raise Exception(msg)
        sortedRow = random.sample([1,2],1)[0]      # sorteia a linha em que estará o Participant no Latin Square
        if sortedRow==1:
            self.row1Participant = participant
        else:
            self.row2Participant = participant            

    def initColumn(self, group):
        tasks = Task.objects.filter(taskGroup=group).values_list('pk', flat=True)                
        randomTasks = random.sample(list(tasks), len(tasks))
        # converte em string (inteiros separados por vírgulas) e retorna
        return ",".join(str(x) for x in randomTasks)

    def setNewParticipant(self, participant):
        if self.row1Participant==None:
            self.row1Participant = participant
        else:
            self.row2Participant = participant     

    def isDt(self, row, column):
        return self.cells[row][column]

    class Meta:
        db_table="ms_latinSquare" 
    

class DTModel(models.Model):
    dtImg = models.CharField(max_length=50)    
    dtNumberOfLeaves = models.IntegerField()
    dtDepth = models.IntegerField(null=True)       
    dtNodes = models.CharField(max_length=500)

    def __str__(self):
        return self.dtImg
    
    class Meta:
        db_table="ms_dtModel"    

    def getNodesGlossary(self):
        pyPath = os.path.dirname(os.path.abspath(__file__))
        dfMetrics =  pd.read_csv(pyPath + '/software_class_level_metrics.csv', sep=';')        
        # filtra apenas as métricas contidas no nó da árvore exibida
        dfMetrics=dfMetrics[dfMetrics['apiname'].isin(self.dtNodes.split(','))]
        # retira os NaNs e substitui por None
        dfMetrics = dfMetrics.where(pd.notnull(dfMetrics), None)
        return dfMetrics.to_dict('records')


class Task(models.Model):            
    OPTIONS_CS_SCOPE = (('C','Class'),('M','Method'))
    OPTIONS_TASK_GROUP = ((1,'Group 1'),(2,'Group 2')) 
    taskGroup = models.IntegerField(choices=OPTIONS_TASK_GROUP)  # Grupo = coluna do LatinSquare
    codeSmellScope = models.CharField(max_length=1, choices=OPTIONS_CS_SCOPE)
    codeSmellType = models.CharField(max_length=10)
    codeSnippetProject = models.CharField(max_length=100)
    codeSnippetKind = models.CharField(max_length=30)
    codeSnippetURI = models.CharField(max_length=200)
    codeSnippetContent = models.TextField()     
    decisionTree = models.ForeignKey(DTModel, on_delete=models.DO_NOTHING)       
    
    def __str__(self):
        return "Task Group: {0}, CS scope: {1}, CS Type: {2}".format(self.taskGroup, self.codeSmellScope, self.codeSmellType)
    
    def getForm(self, post=None, instance=None):        
        from django.forms import ChoiceField
        from . import forms  
        form = forms.AnswerTaskIDForm(post, instance=instance)
        if(self.codeSmellScope=='C'):
            choices = (                                                    
                        ('CDSBP','CLASS DATA SHOULD BE PRIVATE - A class exposing its fields, violating the principle of data hiding.'),
                        ('CC','COMPLEX CLASS - A class having at least one method having a high cyclomatic complexity.'),
                        ('GC','GOD CLASS - A large class implementing different responsibilities and centralizing most of the system processing.'),
                        ('II','INAPPROPRIATE INTIMACY - Two classes exhibiting a very high coupling between them.'),
                        ('LC','LAZY CLASS - A class having very small dimension, few methods and low complexity.'),
                        ('MM','MIDDLE MAN - A class delegating to other classes most of the methods it implements.'),
                        ('RB','REFUSED BEQUEST - A class redefining most of the inherited methods, thus signaling a wrong hierarchy.'),
                        ('SC','SPAGHETTI CODE - A class implementing complex methods interacting between them, with no parameters, using global variables.'),
                        ('SG','SPECULATIVE GENERALITY - A class declared as abstract having very few children classes using its methods.'),
                        )
        else:
            choices = (                                                    
                        ('LM','LONG METHOD - A method that is unduly long in terms of lines of code.'),
                        ('LPL','LONG PARAMETER LIST - A method having a long list of parameters, some of which avoidable.'),
                        ('FE','FEATURE ENVY - Refers to methods that use much more data from other classes than from their own class. A Feature Envy tends to use more attributes from other classes than from its own class, and to use many attributes from few different classes.'),
                        )
        form.fields['answer_cst'].choices = choices
        return form
            
    class Meta:
        db_table="ms_task"      

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
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    secondsToAnswer = models.FloatField(null=True) 
    isDt = models.BooleanField(default=False)
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
