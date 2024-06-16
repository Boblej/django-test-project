from django.contrib import admin
from django.urls import path, include
from cafe_restaurant.views import home_view, register_view, contact_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', include('menu.urls')),
    path('reservations/', include('reservations.urls')),
    path('promotions/', include('promotions.urls')),
    path('reviews/', include('reviews.urls')),
    path('accounts/', include('accounts.urls')),
    path('register/', register_view, name='register'),
    path('contact/', contact_view, name='contact'),
    path('', home_view, name='home'),
]
