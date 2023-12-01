
from django.urls import path
from . import views as views
urlpatterns = [
    path('dangki/', views.regisiter,name='regisiter'),
    
]