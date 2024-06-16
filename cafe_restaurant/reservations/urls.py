from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation_list, name='reservation_list'),
    path('new/', views.reservation_form, name='reservation_form'),
]
