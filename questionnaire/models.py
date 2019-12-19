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
        dfMetricsClass =  pd.read_csv(pyPath + '/software_class_level_metrics.csv', sep=';')        
        dfMetricsMethod =  pd.read_csv(pyPath + '/software_method_level_metrics.csv', sep=';')        
        dfMetrics = dfMetricsClass.append(dfMetricsMethod)        
        # filtra apenas as métricas contidas no nó da árvore exibida
        dfMetrics=dfMetrics[dfMetrics['apiname'].isin(self.dtNodes.split(','))]
        # retira possíveis repetições
        dfMetrics = dfMetrics.drop_duplicates(subset=['apiname'])
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
        return "Id: {3}, Task Group: {0}, CS scope: {1}, CS Type: {2}".format(self.taskGroup, self.codeSmellScope, self.codeSmellType, self.id)
    
    def getForm(self, post=None, instance=None):        
        from django.forms import ChoiceField
        from . import forms  
        form = forms.AnswerTaskIDForm(post, instance=instance)        
        return form

    def getCsDescription(self):
        csDescriptions = {'gc':'GOD CLASS;A large class implementing different responsibilities and centralizing most of the system processing.',
                            'lpl':'LONG PARAMETER LIST;A method having a long list of parameters, some of which avoidable.',
                            'lm':'LONG METHOD;A method that is unduly long in terms of lines of code.',
                            'mm':'MIDDLE MAN;A class delegating to other classes most of the methods it implements.',
                            'cdsbp':'CLASS DATA SHOULD BE PRIVATE;A class exposing its fields, violating the principle of data hiding.',
                            }
        return csDescriptions[self.codeSmellType].split(';')

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
    OPTIONS_CODE_AGREEMENT = (
            (2, "Strongly Agree"),
            (1, "Agree"),                  
            (-1, "Disagree"),
            (-2, "Strongly Disagree"),
            )
    questionnaire = models.ForeignKey(Questionnaire,on_delete=models.CASCADE)    
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    secondsToAnswer = models.FloatField(default=0) 
    isDt = models.BooleanField(default=False)
    class Meta:
        db_table="ms_answer"  

# Classe para respostas da task
class AnswerTaskID(Answer):           
    answer_csagreement = models.IntegerField(choices=Answer.OPTIONS_CODE_AGREEMENT, default=None)
    answer_description = models.TextField()
    class Meta:
        db_table="ms_answerTaskID"

class InviteControl(models.Model):
    inviteId = models.CharField(primary_key=True,unique=True,max_length=10)
    activated = models.BooleanField(default=False)
    class Meta:
        db_table="ms_inviteControl"
