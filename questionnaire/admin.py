from django.contrib import admin

# Register your models here.
from .models import Participant
from .models import Questionnaire, AnswerTaskID, Answer, LatinSquare
from .models import Task, DTModel

admin.site.register(Participant)
admin.site.register(Task)
admin.site.register(DTModel)
admin.site.register(Questionnaire)
admin.site.register(AnswerTaskID)
admin.site.register(Answer)
admin.site.register(LatinSquare)
