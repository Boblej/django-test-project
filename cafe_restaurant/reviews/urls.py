from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_list, name='review_list'),
    path('new/', views.review_create, name='review_create'),
    path('contact/', views.contact_info, name='contact_info'),
]
