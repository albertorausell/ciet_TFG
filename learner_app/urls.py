
from django.urls import path
from learner_app import views


urlpatterns = [
    path('capabilities/', views.capabilities, name='capabilities_learner'),
    path('evaluations/', views.evaluations, name='evaluations_learner'),
    path('ranking/', views.ranking, name='ranking_learner'),

    path('capabilities/<int:id>/', views.capability_details,
         name='capability_details'),

    path('capabilities/<int:id>/show', views.capability_show,
         name='capability_show'),

    path('evaluations/increase_mark/<int:id>', views.increase_mark,
         name='increase_mark'),
]
