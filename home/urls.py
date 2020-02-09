from django.urls import path
from django.conf.urls import include, url
from . import views
from .views import *

app_name = 'home'
urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home_list'),
    path('idabax19', view=views.home19, name='home19'),
    path('speaker19', view=views.speakers19, name='speaker19'),
]
