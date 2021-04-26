
from django.urls import path
from trainer_app import views


urlpatterns = [
    path('capabilities/', views.capabilities, name='capabilities_trainer'),
    path('objectives/', views.objectives, name='objectives_trainer'),
    path('statistics/', views.statistics, name='statistics_trainer'),

    path('objectives/edit/<int:id>/', views.objective_edit, name='objective_edit')
]
