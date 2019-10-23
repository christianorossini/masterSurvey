from django.contrib import admin

# Register your models here.
from .models import Participant
from .models import Question
from .models import Task

admin.site.register(Participant)
admin.site.register(Task)
admin.site.register(Question)
