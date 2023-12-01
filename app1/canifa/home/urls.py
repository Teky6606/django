
from django.urls import path
from . import views as views
urlpatterns = [
    path('dangki/', views.regisiter,name='regisiter'),
    path('about/', views.getAbout,name='About'),
    path('', views.getHome,name='Home'),
    
]