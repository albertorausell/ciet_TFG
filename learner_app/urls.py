
from django.urls import path
from learner_app import views


urlpatterns = [
    path('capabilities/', views.capabilities, name='capabilities_learner'),
    path('evaluations/', views.evaluations, name='evaluations_learner'),
    path('ranking/', views.ranking, name='ranking_learner')
]
