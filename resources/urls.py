from django.conf.urls import include, url
from . import views
from .views import *


app_name = 'resources'
urlpatterns = [
    url(r'^$', SlideView.as_view(), name='resources_list'),
    url(r'^/photos', PhotoView.as_view(), name='photo_list'),
    url(r'^/videos', VideoView.as_view(), name='video_list'),
]