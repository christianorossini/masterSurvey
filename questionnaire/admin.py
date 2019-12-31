from django.contrib import admin

# Register your models here.
from .models import Participant
from .models import Questionnaire, AnswerTaskID, Answer, LatinSquare
from .models import Task, DTModel

admin.site.register(Participant)
#admin.site.register(Task)
#admin.site.register(DTModel)
admin.site.register(Questionnaire)
admin.site.register(AnswerTaskID)
admin.site.register(Answer)
#admin.site.register(LatinSquare)


class TaskAdmin(admin.ModelAdmin):
    list_display =  [f.name for f in Task._meta.fields if f.name != "codeSnippetContent"]    
admin.site.register(Task, TaskAdmin)

class DTModelAdmin(admin.ModelAdmin):
    list_display =  [f.name for f in DTModel._meta.fields]    
admin.site.register(DTModel, DTModelAdmin)

class LatinSquareAdmin(admin.ModelAdmin):
    list_display =  [f.name for f in LatinSquare._meta.fields]    
admin.site.register(LatinSquare, LatinSquareAdmin)