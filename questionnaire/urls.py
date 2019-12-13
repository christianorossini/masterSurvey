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