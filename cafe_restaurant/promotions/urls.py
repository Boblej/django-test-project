from django.urls import path
from .views import PromotionListView, PromotionDetailView, EventListView, EventDetailView

urlpatterns = [
    path('promotions/', PromotionListView.as_view(), name='promotion_list'),
    path('promotions/<int:pk>/', PromotionDetailView.as_view(), name='promotion_detail'),
    path('events/', EventListView.as_view(), name='event_list'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
]
