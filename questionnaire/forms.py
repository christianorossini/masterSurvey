from .models import *
from django.forms import ModelForm, CharField, TextInput, Select, RadioSelect, HiddenInput, Textarea, NumberInput, IntegerField
from django import forms


class ParticipantForm(ModelForm):
    class Meta:
        model = Participant        
        exclude = ['inviteId']
        widgets = {            
        }
        labels = {
            'degree': '1 - What is your highest degree in computing or related fields?',            
            'origin': '2 - Where do you come from?',            
            'yearsDevExperience': '3 - Amount of experience in software development (years):',            
            'devExperience': '4.1 - Software development:',    
            'objOrientedExperience': '4.2 - Object oriented development:',            
            'javaExperience': '4.3 - Development with java:',
            'codeRevision': '4.4 - Code revision:',  
            'codeSmellIdentification': '4.5 - Code smells identification:',
        }


class AnswerTaskForm(forms.ModelForm):        
    class Meta:               
       model = AnswerTaskID
       fields = ['answer_csagreement', 'answer_description', 'questionnaire', 'task', 'secondsToAnswer']
       widgets = {            
           'answer_csagreement': RadioSelect(),                       
           'answer_description': Textarea(attrs={'class':"form-control", 'rows':'5'}),           
           'questionnaire': HiddenInput(),           
           'task': HiddenInput(),  
           'secondsToAnswer': HiddenInput(),           
       }
       labels = {
            'answer_csagreement': '1 - Do you agree?',
            'answer_description': '2 - Could you please justify your choice above?',
        }
                
class AnswerTaskDTForm(AnswerTaskForm):        
    class Meta:            
        model = AnswerTaskID
        exclude = ['devExperience_qtdYears','devExperience_qtdProjects','devExperience_qtdProjectsIndustry','objOrientedExperience_qtdYears','objOrientedExperience_qtdProjects','objOrientedExperience_qtdProjectsIndustry','javaExperience_qtdYears','javaExperience_qtdProjects','javaExperience_qtdProjectsIndustry','codeRevision_qtdYears','codeRevision_qtdProjects','codeRevision_qtdProjectsIndustry','codeSmellIdentification_qtdYears','codeSmellIdentification_qtdProjects','codeSmellIdentification_qtdProjectsIndustry']
        fields = ['answer_csagreement', 'answer_description', 'questionnaire', 'task', 'secondsToAnswer','answer_dtDescription']
        widgets = {            
           'answer_csagreement': RadioSelect(),                       
           'answer_description': Textarea(attrs={'class':"form-control", 'rows':'5'}),
           'answer_dtDescription': Textarea(attrs={'class':"form-control", 'rows':'5'}),
           'questionnaire': HiddenInput(),           
           'task': HiddenInput(),  
           'secondsToAnswer': HiddenInput(),           
        }
        labels = {
            'answer_csagreement': '1 - Do you agree?',
            'answer_description': '2 - Could you please justify your choice above?',
            'answer_dtDescription': '3 - What insights (contributions) did the decision tree give you in order to support your decision?',            
        }

        
