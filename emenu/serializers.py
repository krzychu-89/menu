import os

from django.conf import settings
from rest_framework import serializers

from menu_test.settings import MEDIA_ROOT, MEDIA_URL, \
    LOGS_TIMESTAMP, current_timezone
from .models import *
import pytz
import datetime


class MenuSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format=LOGS_TIMESTAMP,
                                        required=False, read_only=True)
    modified = serializers.DateTimeField(format=LOGS_TIMESTAMP,
                                         required=False, read_only=True)
    num_dishes = serializers.IntegerField(required=False)

    def to_representation(self, instance):
        representation = super(MenuSerializer, self).to_representation(instance)
        representation['created'] = convert_datetime(instance['created'])
        representation['modified'] = convert_datetime(instance['modified'])
        return representation

    class Meta:
        model = Menu
        fields = ["id", "name", "description", "created",
                  "modified", "num_dishes"]


class DishSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format=LOGS_TIMESTAMP,
                                        required=False, read_only=True)
    modified = serializers.DateTimeField(format=LOGS_TIMESTAMP,
                                         required=False, read_only=True)
    image = serializers.SerializerMethodField()

    def to_representation(self, instance):
        representation = super(DishSerializer, self).to_representation(instance)
        representation['created'] = convert_datetime(instance['created'])
        representation['modified'] = convert_datetime(instance['modified'])
        return representation

    def get_image(self, instance):
        request = self.context.get('request')
        relative_url = instance['image']
        if relative_url:
            full_url = os.path.join(MEDIA_URL, relative_url)
        else:
            full_url = ''
        return full_url

    class Meta:
        model = Dish
        fields = ["id", "name", "description", "preparation_time",
                  "is_vegetarian", "created", "modified", "image"]

def convert_datetime(data, format=None):
    if not format:
        format = LOGS_TIMESTAMP
    else:
        format = format
    if isinstance(data, datetime.datetime):
            correct_datetime = data.astimezone(pytz.timezone(current_timezone))
            data = correct_datetime.strftime(format)
    return data