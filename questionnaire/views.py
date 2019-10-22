from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
#from .models import Question, Choice
from .forms import ParticipantForm

# Create your views here.
def index(request):
    return render(request, 'masterquest/index.html')

def login(request):
    return render(request, 'masterquest/login.html')

def newparticipant(request):
    if(request.method=='POST'):
        form = ParticipantForm(request.POST)
    else:
        form = ParticipantForm()    
    return render(request, 'masterquest/participant.html', {'form': form})    

def detail(request, question_id):
   """  question = get_object_or_404(Question, pk=question_id)
    return render(request, 'masterquest/detail.html', {'question': question}) """    

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
    