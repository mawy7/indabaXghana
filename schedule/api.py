from rest_framework.viewsets import ModelViewSet

from .serializers import DaySerializer, SpeakerScheduleSerializer, TalkSerializer, EventSerializer
from .models import Day, SpeakerSchedule, Event
from speakers.models import Speaker


class DayViewSet(ModelViewSet):
    queryset = Day.objects.all()
    serializer_class = DaySerializer


class SpeakerScheduleViewSet(ModelViewSet):
    queryset = SpeakerSchedule.objects.all()
    serializer_class = SpeakerScheduleSerializer


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer