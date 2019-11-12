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


class AnswerTaskIDForm(forms.ModelForm):        
    class Meta:               
       model = AnswerTaskID
       fields = ['answerq1', 'answerq1_complement', 'answerq2', 'answerq2_complement', 'questionnaire', 'dtModel', 'task']
       widgets = {            
           'answerq1': Select(attrs={'class':"form-control"}),            
           'answerq1_complement': TextInput(attrs={'class':"form-control"}),
           'answerq2': RadioSelect(),
           'answerq2_complement': TextInput(attrs={'class':"form-control"}),                 
           'questionnaire': HiddenInput(),
           'dtModel': HiddenInput(),
           'task': HiddenInput(),            
       }
                
class AnswerTaskCCForm(forms.ModelForm):        
    class Meta:               
        model = AnswerTaskCC
        fields = ['answerq1', 'answerq1_complement', 'answerq2', 'answerq2_complement','questionnaire', 'dtModel', 'task']
        widgets = {            
            'answerq1': Select(attrs={'class':"form-control"}), 
            'answerq1_complement': TextInput(attrs={'class':"form-control"}),  
            'answerq2': RadioSelect(),
            'answerq2_complement': TextInput(attrs={'class':"form-control"}),            
            'questionnaire': HiddenInput(),
            'dtModel': HiddenInput(),
            'task': HiddenInput(),        
        }

        
