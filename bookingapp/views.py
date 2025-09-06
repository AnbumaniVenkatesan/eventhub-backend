from django.shortcuts import render
from rest_framework import viewsets
from .models import Event, Booking
from .serializers import EventSerializer, BookingSerializer

# Event API
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

# Booking API
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

