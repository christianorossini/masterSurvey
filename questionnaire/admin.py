from django.contrib import admin

# Register your models here.
from .models import Participant
from .models import Question, Questionnaire, AnswerTaskCL, AnswerTaskID, AnswerTaskRA, Answer
from .models import Task, DTModel

admin.site.register(Participant)
admin.site.register(Task)
admin.site.register(Question)
admin.site.register(DTModel)
admin.site.register(Questionnaire)
admin.site.register(AnswerTaskCL)
admin.site.register(AnswerTaskID)
admin.site.register(AnswerTaskRA)
admin.site.register(Answer)
