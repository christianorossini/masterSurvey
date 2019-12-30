from .models import *
from django.forms import ModelForm, CharField, TextInput, Select, RadioSelect, HiddenInput, Textarea
from django import forms


class ParticipantForm(ModelForm):
    class Meta:
        model = Participant        
        exclude = ['inviteId']
        widgets = {            
            'experience': Select(attrs={'class':"form-control"}),
            'dsIndustryRole': Textarea(attrs={'class':"form-control", 'rows':'3'}),           
            'dsDevelopmentExperience': Textarea(attrs={'class':"form-control", 'rows':'3'}),
        }
        labels = {
            'degree': '1 - What is your highest degree in computing or related fields?',            
            'dsIndustryRole': '2 - Are you in the industry right now? If so, what is your current main role?',            
            'dsDevelopmentExperience': '3 - In the text box below, make a briefly overview of your experience in software development.',            
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

        
