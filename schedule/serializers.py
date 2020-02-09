from rest_framework import serializers

from schedule.models import SpeakerSchedule, Event, Day
from speakers.models import Speaker


class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ('conference_day')


class SpeakerScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeakerSchedule
        fields = all


class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        exclude = ('twitter', 'website', 'biography')


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = all