from django.shortcuts import render, render_to_response
from django.views.generic import ListView
from django.template import RequestContext
from django.views.generic.detail import DetailView
from .models import Sponsor
# Create your views here.


class HomeView(ListView):
   model = Sponsor
   template_name = 'home.html'
   context_object_name = 'sponsors'


def home19(request):
    context = {}
    template = 'home19.html'
    return render(request, template, context)

def speakers19(request):
    context = {}
    template = 'speakers19.html'
    return render(request, template, context)

def handler404(request, exception):
    return render(request, '404.html', locals())