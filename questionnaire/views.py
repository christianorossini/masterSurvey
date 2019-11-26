from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
import secrets
from .forms import ParticipantForm, AnswerTaskCCForm, AnswerTaskIDForm
from .models import DTModel, Task, Answer, Questionnaire
import random
import datetime

# Create your views here.
def index(request):
    return render(request, 'masterquest/index.html')

def login(request):
    return render(request, 'masterquest/login.html')

def newparticipant(request):
    if(request.method=='POST'):
        form = ParticipantForm(request.POST)
        
        if(form.is_valid):            
            participant = form.save(commit=False)
            participant.inviteId = secrets.token_hex(5) #atribuição manual do inviteId, enquanto se estuda o uso do atributo
            participant.save()

            #cria um novo questionário e vincula o participant
            # TODO tentar realizar um save só
            questionnaire = Questionnaire()            
            questionnaire.participant = participant
            questionnaire.save()                        

            #inclui o participante na sessão, condiciona acessar os outros passos da survey a partir desta view
            request.session['participant']=participant.inviteId
            request.session['participantName']=participant.name
            request.session['questionnaireID']=questionnaire.id

            initSurvey(request)

            return HttpResponseRedirect(reverse('instructions'))     

    else:
        form = ParticipantForm()    
    
    return render(request, 'masterquest/participant.html', {'form': form})    

def instructions(request):    
    if(not isParticipantInSession(request)):
        return HttpResponseRedirect(reverse('index'))

    return render(request, 'masterquest/instructions.html')

def survey(request):
    if(not isSurveyInitiated(request)):
        return HttpResponseRedirect(reverse('index'))      
    
    pkModel = request.session['dtModelSequenceList'][getCurrentDtModelIndex(request)]
    pkTask = request.session['taskSequenceList'][getCurrentTaskIndex(request)]        
    dtModel = DTModel.objects.get(pk=pkModel)
    task = Task.objects.get(pk=pkTask)
    questionnaire = Questionnaire.objects.get(pk=request.session['questionnaireID'])         
    
    if(request.method=='POST'):
        
        ## TODO código redundante: refatorar
        pkTask = request.session['taskSequenceList'][getCurrentTaskIndex(request)]
        task = Task.objects.get(pk=pkTask)
        ##
        answerForm = task.getForm(post=request.POST)

        if(answerForm.is_valid()):
            answerForm.save()
        
            # fim do survey
            if(isLastDtModel(request) and isLastTask(request)):
                return HttpResponseRedirect(reverse('finish'))  
           
            # próximo classification tree
            if(isLastTask(request)):
                nextDtModel(request)
                setCurrentTaskIndex(request, 0)
            else:
                #próxima task
                nextTask(request)
            
            return HttpResponseRedirect(reverse('survey'))
    else:       
        answer = Answer()
        answer.dtModel = dtModel 
        answer.questionnaire = questionnaire
        answer.task = task        
        answerForm = task.getForm(instance=answer)        
    
    return render(request, task.getView(), context={'dtModel':dtModel, 'task':task, 'form':answerForm, 
                'questions':task.questions.all(), 'classificationTreePosition':getCurrentDtModelIndex(request)+1, 
                'classificationTreeTotal':len(request.session['dtModelSequenceList'])})

def endSurvey(request):
    if(not isSurveyInitiated(request)):
        return HttpResponseRedirect(reverse('index'))
       
    #encerra o questionário
    questId = request.session['questionnaireID']
    questionnaire = Questionnaire.objects.get(id=questId)
    questionnaire.finish()
    questionnaire.save()
    
    #elimina as varíáveis de controle criadas para gerenciar o survey
    del request.session['participant']
    del request.session['participantName']
    del request.session['dtModelSequenceList']
    del request.session['taskSequenceList']
    del request.session['questionnaireID']
        
    return render(request, 'masterquest/surveyFinish.html')

def results(request, question_id):
   """  question = get_object_or_404(Question, pk=question_id)
    return render(request, 'masterquest/results.html', {'question': question}) """

def vote(request, question_id):
   """  question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'masterquest/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', args=(question.id,))) """
 
def isParticipantInSession(request):
    if('participant' in request.session):
         return HttpResponseRedirect(reverse('newparticipant'))   
 
#inicializa o survey. Cria um fluxo com a sequência de atividades
def initSurvey(request):    
    modelSequencePks = list(DTModel.objects.values_list('pk', flat=True))
    # embaralha a ordem das models para que cada participante execute a survey em uma ordem diferente
    random.shuffle(modelSequencePks)
    # guarda a ordem das models embaralhadas em variável de sessão
    request.session['dtModelSequenceList'] = modelSequencePks
    taskSequencePks = list(Task.objects.values_list('pk', flat=True).order_by('sequenceNumber'))    
    request.session['taskSequenceList'] = taskSequencePks
    setCurrentTaskIndex(request, 0)
    setCurrentDtModelIndex(request, 0)

def isSurveyInitiated(request):
    return 'dtModelSequenceList' in request.session

def nextTask(request):    
    currentTaskIndex = getCurrentTaskIndex(request) + 1            
    setCurrentTaskIndex(request, currentTaskIndex)
    return request.session['taskSequenceList'][currentTaskIndex]

def nextDtModel(request):
    currentModelIndex = getCurrentDtModelIndex(request) + 1        
    setCurrentDtModelIndex(request, currentModelIndex)    
    return request.session['dtModelSequenceList'][currentModelIndex]

def isLastTask(request):
    currentTask = getCurrentTaskIndex(request)
    taskList = request.session['taskSequenceList']
    return len(taskList)==currentTask+1

def isLastDtModel(request):
    currentModel = getCurrentDtModelIndex(request)
    modelList = request.session['dtModelSequenceList']
    return len(modelList)==currentModel+1

def setCurrentTaskIndex(request, num):
    request.session['currentTask'] = num

def getCurrentTaskIndex(request):
    return request.session['currentTask']

def setCurrentDtModelIndex(request, num):
    request.session['currentDTModel'] = num

def getCurrentDtModelIndex(request):
    return request.session['currentDTModel']


    
