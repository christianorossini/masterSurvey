from .models import *
from django.forms import ModelForm, CharField, TextInput, Select, RadioSelect, HiddenInput
from django import forms


class ParticipantForm(ModelForm):
    class Meta:
        model = Participant        
        exclude = ['inviteId']
        widgets = {
            'name': TextInput(attrs={'class':"form-control"}),
            'experience': Select(attrs={'class':"form-control"}),
            'origin': Select(attrs={'class':"form-control"}),
        }


class AnswerTaskCLForm(forms.ModelForm):        
    class Meta:               
        model = AnswerTaskCL
        fields = ['answerq1', 'answerq2', 'questionnaire', 'dtModel', 'task', 'secondsToAnswer']
        widgets = {            
            'answerq1': Select(attrs={'class':"form-control slcQuest1"}),
            'answerq2': Select(attrs={'class':"form-control slcQuest2"}),
            'questionnaire': HiddenInput(),
            'dtModel': HiddenInput(),
            'task': HiddenInput(),
            'secondsToAnswer': HiddenInput(),
        }

class AnswerTaskRAForm(forms.ModelForm):        
    class Meta:               
        model = AnswerTaskRA
        fields = ['answerq1', 'questionnaire', 'dtModel', 'task']
        widgets = {            
            'answerq1': RadioSelect(),            
            'questionnaire': HiddenInput(),
            'dtModel': HiddenInput(),
            'task': HiddenInput(),            
        }