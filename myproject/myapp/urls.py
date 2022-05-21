from django.urls import path
from . import views
from .views import *

urlpatterns = [

    path('', views.show_main, name="home"),
    path('home/', views.show_main, name="home"),
    path('register/', views.student_register, name="student_register"),
    path('status/', views.show_status, name="status"),
    path('balance/', views.show_balance, name="balance"),

]