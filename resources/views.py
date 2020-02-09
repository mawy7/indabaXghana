from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import ListView
from django.template import RequestContext
from django.views.generic.detail import DetailView
from .models import Slide, Photo, Video
from hitcount.views import HitCountDetailView






class SlideView(ListView):
   model = Slide
   template_name = 'resources.html'
   context_object_name = 'slides'


class PhotoView(ListView):
   model = Photo
   template_name = 'photo.html'
   context_object_name = 'photos'



class VideoView(ListView):
   model = Video
   template_name = 'video.html'
   context_object_name = 'videos'

