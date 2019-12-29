from django.urls import path

from . import views

#app_name = 'masterquest'
urlpatterns = [    
    path('', views.index, name='index'),    
    path('login/', views.login, name='login'),
    path('newparticipant/', views.newparticipant, name='newparticipant'),
    path('instructions/<str:participant_id>', views.instructions, name='instructions'),
    path('startSurvey/', views.startSurvey, name='startSurvey'),    
    path('survey/', views.survey, name='survey'),    
    path('finish/', views.endSurvey, name='finish'),    
    path('warmup1/<str:participant_id>', views.warmup, name='warmup1'),    
    path('instructions2/<str:participant_id>', views.instructions2, name='instructions2'),    
    path('warmup2/<str:participant_id>', views.warmup, name='warmup2'),    
    path('instructions3/<str:participant_id>', views.instructions3, name='instructions3'),    
    # ex: /polls/5/results/
    #path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]

""" urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
] """