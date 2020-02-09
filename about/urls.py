from django.conf.urls import include, url
from . import views
from .views import *


app_name = 'about'
urlpatterns = [
    url(r'^$', AboutListView.as_view(), name='about_list'),
    url(r'^/<slug:slug>/', AboutDetailView.as_view(), name='about_detail'),
]