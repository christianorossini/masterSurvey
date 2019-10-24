from django.contrib import admin

# Register your models here.
from .models import Participant
from .models import Question
from .models import Task, DTModel

admin.site.register(Participant)
admin.site.register(Task)
admin.site.register(Question)
admin.site.register(DTModel)
