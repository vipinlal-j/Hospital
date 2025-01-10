from django.urls import path
from WebApp import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('book_appointment_guest/', views.book_appointment_guest, name="book_appointment_guest"),
    path('save_appointment_guest/', views.save_appointment_guest, name="save_appointment_guest")

]