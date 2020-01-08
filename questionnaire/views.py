from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseNotFound, HttpResponseForbidden
from django.template import loader
from django.urls import reverse
from django.db import IntegrityError

from .forms import ParticipantForm, AnswerTaskForm, AnswerTaskDTForm
from .models import DTModel, Task, Answer, Questionnaire, LatinSquare, Participant
import random
import datetime
from .surveyManager import SurveyManager

# Create your views here.
def index(request):
    return render(request, 'masterquest/index.html')

def login(request):
    return render(request, 'masterquest/login.html')

def newparticipant(request):
    if(request.method=='POST'):
        form = ParticipantForm(request.POST)
        
        if form.is_valid():            
            participant = form.save(commit=False)  
            participant.save()                                         

            return HttpResponseRedirect(reverse('instructions', args=(participant.pk,)))     

    else:
        form = ParticipantForm()    
    
    return render(request, 'masterquest/participant.html', {'form': form})    


def instructions(request, participant_id):    
    get_object_or_404(Participant, pk=participant_id)
    numTasks = Task.objects.count()    
    return render(request, 'masterquest/instructions.html', context={'participant_id':participant_id, 'numTasks':numTasks, 'numTasksHalf':numTasks/2})


def warmup(request, participant_id):     
    get_object_or_404(Participant, pk=participant_id)
        
    surveyManager = SurveyManager(request)
    task = surveyManager.getWarmupTask()   
    
    if(request.path_info.find('warmup1')>0):
        answerForm = AnswerTaskForm()
        showTree = False
        nextView = 'instructions2'
    else:
        answerForm = AnswerTaskDTForm()
        showTree = True
        nextView = 'instructions3'

    return render(request, "masterquest/survey_warmup.html", 
                context={'dtModel':task.decisionTree, 'task':task, 'form':answerForm, 'showTree': showTree, 'participant_id':participant_id, 'nextView':nextView})


def instructions2(request, participant_id):
    get_object_or_404(Participant, pk=participant_id)
    return render(request, 'masterquest/instructions2.html', context={'participant_id':participant_id})

def instructions3(request, participant_id):
    get_object_or_404(Participant, pk=participant_id)
    numTasks = Task.objects.count()    
    return render(request, 'masterquest/instructions3.html', context={'participant_id':participant_id, 'numTasks':numTasks, 'numTasksHalf':numTasks/2})

def startSurvey(request):
    if request.method=='POST':
        participant = get_object_or_404(Participant, pk=request.POST['participant_id'])  

        # TODO criar uma condição para evitar que se inicialize várias surveys para o mesmo participant        
        surveyManager = SurveyManager(request)
        try:
            surveyManager.startSurvey(participant)
        except IntegrityError as error:             #verificação caso o mesmo usuário (mesmo identificador) tente iniciar o survey mais de 1 vez
            return HttpResponseForbidden()
        
        return HttpResponseRedirect(reverse('survey'))    

    else:
        return HttpResponseNotFound()
    

def survey(request):
    surveyManager = SurveyManager(request)
    
    if(not surveyManager.isSurveyInitiated()):
        return HttpResponseNotFound(content="Access not allowed.")     
       
    task = Task.objects.get(pk=surveyManager.getCurrentTaskId())
    questionnaire = Questionnaire.objects.get(participant=surveyManager.getParticipantId())
    
    if(request.method=='POST'):
        
        answerForm = surveyManager.getForm(post=request.POST)

        if(answerForm.is_valid()):
            answer = answerForm.save(commit=False)
            answer.isDt = LatinSquare().isDt(surveyManager.getCurrentRow(),surveyManager.getCurrentColumn()) # atribui à resposta se a tarefa foi DT ou noDT
            answer.save()
            try:
                surveyManager.nextTask()
                return HttpResponseRedirect(reverse('survey'))
            except IndexError:
                # esgotou o número de atividades programadas para o participante, encerra o survey
                surveyManager.finishSurvey()
                return HttpResponseRedirect(reverse('finish'))             
    else:       
        answer = Answer()        
        answer.questionnaire = questionnaire
        answer.task = task        
        answerForm =  surveyManager.getForm(instance=answer)        
    
    return render(request, "masterquest/survey.html", 
                context={'dtModel':task.decisionTree, 'task':task, 'form':answerForm, 'showTree': surveyManager.showTree(),
                    'surveyProgress': surveyManager.getSurveyProgress(),
                    'showIntro': surveyManager.showIntro()})

def endSurvey(request):
    return render(request, 'masterquest/surveyFinish.html')
