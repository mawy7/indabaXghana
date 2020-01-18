from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', view=views.home, name='home'),
    path('idabax19', view=views.home19, name='home19'),
    path('speaker19', view=views.speakers19, name='speaker19'),
]