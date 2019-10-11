from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Question, Choice
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'masterquest/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'masterquest/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'masterquest/results.html'


def vote(request, question_id):
    ... # same as above, no changes needed.