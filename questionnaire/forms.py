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
       fields = ['answer_cst', 'answer_cst_confidence', 'questionnaire', 'dtModel', 'task']
       widgets = {            
           'answer_cst': Select(attrs={'class':"form-control"}),                       
           'answer_cst_confidence': RadioSelect(),           
           'questionnaire': HiddenInput(),
           'dtModel': HiddenInput(),
           'task': HiddenInput(),            
       }
                
class AnswerTaskCCForm(forms.ModelForm):        
    class Meta:               
        model = AnswerTaskCC
        fields = ['answer_cst', 'answer_cst_confidence','answer_cst_dm', 'answer_tr', 'answer_tr_complement','questionnaire', 'dtModel', 'task']
        widgets = {            
            'answer_cst': Select(attrs={'class':"form-control"}),                       
            'answer_cst_confidence': RadioSelect(),            
            'answer_cst_dm': RadioSelect(),        
            'answer_tr': RadioSelect(),  
            'answer_tr_complement': Textarea(attrs={'class':"form-control", 'rows':'5'}),      
            'questionnaire': HiddenInput(),
            'dtModel': HiddenInput(),
            'task': HiddenInput(),        
        }

        
