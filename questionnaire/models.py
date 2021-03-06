import logging
import os
import random
import secrets
from datetime import datetime

import pandas as pd
from django.db import models


class Participant(models.Model):        
    PARTICIPANT_ORIGIN = (
        ('I', 'Industry - Professional from industry.'),
        ('A', 'Academy - Professional from academy [bacharelor, master or PHD].'),        
        ('B', 'Both - Professional from academy and industry.'),                
    )    
    DEGREES = (        
        ('B', 'Bachelor degree'),
        ('M', 'Master degree'),        
        ('P', 'PHD'),        
        ('N', 'None of them'),
    )
    EXPERIENCE_LEVEL = (
        (0, 'I do not have any experience'),
        (1, 'Very low'),        
        (2, 'Low'),        
        (3, 'High'),        
        (4, 'Very high'),        
    )    
    inviteId = models.CharField(primary_key=True,unique=True,max_length=10)
    degree = models.CharField(max_length=1, choices=DEGREES)
    origin = models.CharField(choices=PARTICIPANT_ORIGIN, max_length=1) 
    yearsDevExperience = models.PositiveIntegerField()
    devExperience = models.IntegerField(choices=EXPERIENCE_LEVEL)
    objOrientedExperience = models.IntegerField(choices=EXPERIENCE_LEVEL)
    javaExperience = models.IntegerField(choices=EXPERIENCE_LEVEL)
    codeRevision = models.IntegerField(choices=EXPERIENCE_LEVEL)
    codeSmellIdentification = models.IntegerField(choices=EXPERIENCE_LEVEL)        
    def save(self):
        self.inviteId = secrets.token_hex(5) #atribuição manual do inviteId, enquanto se estuda o uso do atributo        
        super().save()
    
    # def __str__(self):
    #     return self.name
    
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
    codeSnippet2URI = models.CharField(max_length=200, null=True, blank=True)
    codeSnippet2Content = models.TextField(null=True, blank=True)     
    decisionTree = models.ForeignKey(DTModel, on_delete=models.DO_NOTHING)       
    isDummy = models.BooleanField(default=0)
    
    def __str__(self):
        return "Id: {3}, Task Group: {0}, CS scope: {1}, CS Type: {2}".format(self.taskGroup, self.codeSmellScope, self.codeSmellType, self.id)
    
    def getCsDescription(self):
        csDescriptions = {'gc':'''God Class;1 - A God Class implements several different responsibilities and centralize most of the system processing. 
                                    2 - tends to be complex, to have too much code and many instance variables.''',
                            'rb':'Refused Bequest;1 - A class redefining most of the inherited methods, thus signaling a wrong hierarchy. 2 - Subclasses get to inherit the methods and data of their parents, but they just use a few of them.',
                            'lpl':'Long Parameter List;A method having a long list of parameters, some of which avoidable.',
                            'lm':'Long Method;1 - A method that is unduly long in terms of lines of code. 2 - A method that is too long and tries to do too much.',                            
                            }
                            #'fe':'FEATURE ENVY;Refers to methods that use much more data from other classes than from their own class. A Feature Envy tends to use more attributes from other classes than from its own class, and to use many attributes from few different classes',
                            #'cdsbp':'Class Data Should be private;1. A class exposing its fields, violating the principle of data hiding. 2. A class exposing its attributes.',
                            #'mm':'Middle Man;A class delegating to other classes most of the methods it implements. Middle Man instances arise when a class is delegating all its work to other classes.',                            

                            
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
    OPTIONS_CODE_AGREEMENT = (
            (2, "Agree Strongly"),
            (1, "Agree Slightly"),                  
            (-1, "Disagree Slightly"),            
            (-2, "Disagree Strongly"),
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
    answer_dtDescription = models.TextField(default='')
    class Meta:
        db_table="ms_answerTaskID"

class InviteControl(models.Model):
    inviteId = models.CharField(primary_key=True,unique=True,max_length=10)
    activated = models.BooleanField(default=False)
    class Meta:
        db_table="ms_inviteControl"
