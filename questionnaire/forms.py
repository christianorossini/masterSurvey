from .models import *
from django.forms import ModelForm, CharField, TextInput, Select, RadioSelect
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
        fields = ['answerq1', 'answerq2']
        widgets = {            
            'answerq1': Select(attrs={'class':"form-control"}),
            'answerq2': Select(attrs={'class':"form-control"})
        }