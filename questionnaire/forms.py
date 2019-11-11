from .models import *
from django.forms import ModelForm, CharField, TextInput, Select, RadioSelect, HiddenInput, Textarea
from django import forms


class ParticipantForm(ModelForm):
    class Meta:
        model = Participant        
        exclude = ['inviteId']
        widgets = {
            'name': TextInput(attrs={'class':"form-control"}),
            'experience': Select(attrs={'class':"form-control"}),
            'origin': Select(attrs={'class':"form-control"}),
            'csBackground': Select(attrs={'class':"form-control"}),
            'csdtBackground': Select(attrs={'class':"form-control"}),
            'mlBackground': Select(attrs={'class':"form-control"}),
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

class AnswerTaskIDForm(AnswerTaskRAForm):        
    class Meta(AnswerTaskRAForm.Meta):               
        model = AnswerTaskID
        fields = ['answerq1', 'answerq1_complement', 'answerq2', 'answerq2_complement', 'answerq3', 'answerq3_complement', 'questionnaire', 'dtModel', 'task']
        widgets = {            
            'answerq1': Select(attrs={'class':"form-control"}), 
            'answerq1_complement': TextInput(attrs={'class':"form-control"}),  
            'answerq2': RadioSelect(),
            'answerq2_complement': TextInput(attrs={'class':"form-control"}),
            'answerq3': RadioSelect(),
            'answerq3_complement': TextInput(attrs={'class':"form-control"}),            
            'questionnaire': HiddenInput(),
            'dtModel': HiddenInput(),
            'task': HiddenInput(),        
        }

        
