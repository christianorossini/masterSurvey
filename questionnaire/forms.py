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
        fields = ['answerq1', 'answerq2', 'questionnaire', 'dtModel', 'task']
        widgets = {            
            'answerq1': Select(attrs={'class':"form-control"}),
            'answerq2': Select(attrs={'class':"form-control"}),
            'questionnaire': HiddenInput(),
            'dtModel': HiddenInput(),
            'task': HiddenInput()
        }