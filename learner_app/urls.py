
from django.urls import path
from learner_app import views


urlpatterns = [
    path('capabilities/', views.capabilities),
    path('evaluations/', views.evaluations),
    path('ranking/', views.ranking)
]
