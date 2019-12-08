from .models import LatinSquare, Questionnaire, Participant
from django.db.models import Q

class SurveyManager:

    def __init__(self, request):
        self.request = request
    
    def startSurvey(self, participant):
        # verifica se existe alguma instância de latin square com alguma row aberta à inserção de participante
        latinSquare = LatinSquare.objects.filter(Q(row1Participant__isnull=True) | Q(row2Participant__isnull=True)).first()
        if latinSquare == None:
            #inicializa uma nova Latin Square
            latinSquare = LatinSquare()
            latinSquare.init(participant)
            latinSquare.save()
        else:
            #inicializa atualiza uma Latin Square que já existe
            latinSquare.setNewParticipant(participant)
            latinSquare.save()
        
        #cria um novo questionário e vincula ao participant        
        questionnaire = Questionnaire()            
        questionnaire.participant = participant
        questionnaire.save()
              
        # inicializa as variáveis de sessão que guardarão o estado do survey
        self.setLatinSquareId(latinSquare.id)        
        self.setParticipantId(participant.pk)
        #inicializa a linha e a coluna do e inicializa a primeira atividade do Latim Square
        self.startLatinSquare(latinSquare, participant)


    def startLatinSquare(self, latinSquare, participant):
        if(latinSquare.row1Participant==participant):
            self.setCurrentRow(0)
        else:
            self.setCurrentRow(1)             
        strTasksList = latinSquare.column1Tasks + "," + latinSquare.column2Tasks        
        tasksList =  [int(x) for x in strTasksList.split(',')]        
        self.setCurrentTaskId(tasksList[0])  # escolha a primeira tarefa da lista para ser a primeira a ser executada
        self.setTasksList(tasksList)

    def setTasksList(self, tasksList):
        self.request.session["tasksList"] = tasksList

    def getTasksList(self):
        return self.request.session["tasksList"]
    
    def setCurrentRow(self, row):
        self.request.session["currentRow"] = row

    def getCurrentRow(self):
        return self.request.session["currentRow"]   
    
    def getCurrentColumn(self):        
        tasksList = self.getTasksList()
        numHalfTasks = len(tasksList)/2
        currentTaskPosition = tasksList.index(self.getCurrentTaskId()) + 1        
        # qualifica a coluna atual do Latin Square baseado no posicionamento do ponteiro que guarda o posicionamento da atividade atual        
        if currentTaskPosition<=numHalfTasks:
            return 0
        else:
            return 1
    
    def setParticipantId(self, id):
        self.request.session["participantId"] = id

    def getParticipantId(self):
        return self.request.session["participantId"]    
        
    def setLatinSquareId(self, id):
        self.request.session["latinSquareId"] = id

    def getLatinSquareId(self):
        return self.request.session["latinSquareId"]         
    
    def setCurrentTaskId(self, taskNum):
        self.request.session['currentTaskId'] = taskNum

    def getCurrentTaskId(self):
        return self.request.session['currentTaskId']
    
    def isSurveyInitiated(self):
        return 'tasksList' in self.request.session
       
    def nextTask(self): 
        tasksList = self.getTasksList()  
        currentTaskArrayPosition = tasksList.index(self.getCurrentTaskId())
        try:            
            nextTask = tasksList[currentTaskArrayPosition + 1]
            self.setCurrentTaskId(nextTask)                                
            
        except IndexError as error:
            raise

    def getSurveyProgress(self):
        currentTaskPosition = self.getTasksList().index(self.getCurrentTaskId()) + 1
        totalTasks = len(self.getTasksList())
        return  "code {0} of {1}".format(currentTaskPosition, totalTasks)

    def selectView(self):
        row = self.getCurrentRow()
        column = self.getCurrentColumn()
        cell = LatinSquare.cells[row][column]
        if(cell==True):
            return "masterquest/survey_task_dt.html"    #retorna visualização com decision tree
        else:
            return "masterquest/survey_task_noDt.html"  #retorna visualização sem decision tree

    def finishSurvey(self):
        #encerra o questionário        
        questionnaire = Questionnaire.objects.get(participant=self.getParticipantId())
        questionnaire.finish()
        questionnaire.save()
        
        #elimina as varíáveis de controle (sessão) criadas para gerenciar o survey
        for sessionStr in ["participantId","latinSquareId",'currentTaskId','tasksList',"currentRow"]:
            del self.request.session[sessionStr]

    
