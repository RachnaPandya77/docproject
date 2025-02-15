from django.contrib import admin
from django.urls import path,include
from docapp import views

urlpatterns = [
    path('',views.index),
    path('profile/',views.profile,name='profile'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'),
    path('userlogout/',views.userlogout),
    path('create/', views.create_doctor, name='create_doctor'),
    path('update/<int:pk>/', views.update_doctor, name='update_doctor'),
    path('delete/<int:pk>/', views.delete_doctor, name='delete_doctor'),
    path('book/<int:pk>/', views.book_appointment, name='book_appointment'),
] 