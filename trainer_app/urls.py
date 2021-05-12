
from django.urls import path
from trainer_app import views


urlpatterns = [
    path('capabilities/', views.capabilities, name='capabilities_trainer'),
    path('objectives/', views.objectives, name='objectives_trainer'),
    path('statistics/', views.statistics, name='statistics_trainer'),

    path('objectives/edit/<int:id>/', views.objective_edit, name='objective_edit'),

    path('capabilities/name/<str:id_str>/',
         views.cap_name, name='capability_name'),

    path('capabilities/description_and_image/<int:id>/',
         views.cap_desc, name='description_and_image'),

    path('capabilities/learners/<int:id>/',
         views.cap_learners, name='learners'),

    path('capabilities/objectives/<int:id>/',
         views.cap_objectives, name='objectives'),

    path('capabilities/contents/<int:id>/<int:obj_pos>/<int:cont_pos>/',
         views.cap_contents, name='contents'),
]
