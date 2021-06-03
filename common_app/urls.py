
from django.urls import path
from common_app import views


urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('login/', views.login_req, name='login'),
    path('logout/', views.logout_req, name='logout'),
]
