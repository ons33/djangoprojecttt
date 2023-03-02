from django.urls import path

from .views import *
from . import views
urlpatterns = [
    path('', index),
    path('list/' , list_event, name="list_event"),
    path('affiche/', ListEvents.as_view(), name="Affiche"),
    path('add/', AddEvent.as_view(), name="add"),
    path('update/<event_id>', update, name='update'),
    path('delete/<int:pk>', views.deleteEvent, name="delete"),

]