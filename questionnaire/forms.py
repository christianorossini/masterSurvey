from .models import Participant, Answer
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


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer    
        fields = ['content']   

class AnswerFormCL1(AnswerForm):        
    class Meta(AnswerForm.Meta):
        OPTIONS = (
            ("", ""),
            ("CS", "It belongs to class 'Code smell'"),
            ("NC", "It DOESN'T belongs to class 'Code smell'"))        
        widgets = {            
            'content': Select(attrs={'class':"form-control"}, choices=OPTIONS)
        }

class AnswerFormCL2(AnswerForm):
    class Meta(AnswerForm.Meta):
        OPTIONS = (
            ("", ""),
            ("CDSBP", "Class Data Should Be Private"),
            ("CC", "Complex Class"),
            ("FE", "Feature Envy"),
            ("GC", "God Class"),
            ("II", "Inappropriate Intimacy"),
            ("LC", "Lazy Class"),
            ("LM", "Long Method"),
            ("LPL", "Long Parameter List"),
            ("MM", "Middle Man"),
            ("RB", "Refused Bequest"),
            ("SC", "Spaghetti Code"),
            ("SG", "Speculative Generality"),
            )     
        widgets = {            
            'content': Select(attrs={'class':"form-control"}, choices=OPTIONS)
        }        
    
class AnswerFormCL3(AnswerForm):
    class Meta(AnswerForm.Meta):
        OPTIONS = (
            ("VE", "Very easy - I answered without any problems in less then 7 seconds"),
            ("E", "Easy - I found the answer quite quickly and without major problems"),
            ("M", "Medium"),
            ("D","Difficult - I had to think hard and am I am not sure if I answered correctly."),
            ("VD","Very difficult - Despite thinking hard, my answer is likely to be wrong."))     
        widgets = { 
            'content': RadioSelect(attrs={}, choices=OPTIONS)
        }


    