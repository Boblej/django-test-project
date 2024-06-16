from django.views.generic import ListView, DetailView
from .models import Promotion, Event

class PromotionListView(ListView):
    model = Promotion
    template_name = 'promotions/promotion_list.html'
    context_object_name = 'promotions'

class PromotionDetailView(DetailView):
    model = Promotion
    template_name = 'promotions/promotion_detail.html'
    context_object_name = 'promotion'

class EventListView(ListView):
    model = Event
    template_name = 'promotions/event_list.html'
    context_object_name = 'events'

class EventDetailView(DetailView):
    model = Event
    template_name = 'promotions/event_detail.html'
    context_object_name = 'event'
