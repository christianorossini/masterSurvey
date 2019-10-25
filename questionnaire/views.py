from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
import secrets
from .forms import ParticipantForm
from .models import DTModel, Task
import random

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

            #inclui o participante na sessão, condiciona acessar os outros passos da survey a partir desta view
            request.session['participant']=participant.inviteId
            request.session['participantName']=participant.name

            return HttpResponseRedirect(reverse('instructions'))        

    else:
        form = ParticipantForm()    
    
    return render(request, 'masterquest/participant.html', {'form': form})    

def instructions(request):    
    if(not isParticipantInSession(request)):
         return HttpResponseRedirect(reverse('newparticipant'))  

    return render(request, 'masterquest/instructions.html')

def survey(request):
    if(not isParticipantInSession(request)):
         return HttpResponseRedirect(reverse('newparticipant'))      
        
    """ if('modelExibOrder' not in request.session):
        # primeiro acesso ao survey: prepara uma variável de sessão que vai ditar a ordem de exibição dos modelos
        modelKeys = list(DTModel.objects.values_list('pk', flat=True))
        random.shuffle(modelKeys) 
        request.session['modelExibOrder'] = modelKeys
    else:
        modelKeys = request.session['modelExibOrder'] """

    #implementar um tratamento para lista vazia
    #dtModel = DTModel.objects.get(pk=modelKeys.pop())    
    import pdb;pdb.set_trace()
    dtModel = DTModel.objects.get(pk=1)
    tasks = Task.objects.filter(dtModel=dtModel)

    return render(request, 'masterquest/survey.html', context={'dtModel':dtModel, 'task':tasks[0]})    

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
