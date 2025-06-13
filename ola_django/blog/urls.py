from django.urls import path
from blog import views 
from django.http import HttpResponse



urlpatterns = [
    path('', views.blog),
    path('exemplo/', views.exemplo)

]