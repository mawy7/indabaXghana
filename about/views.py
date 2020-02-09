from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import ListView
from django.template import RequestContext
from django.views.generic.detail import DetailView
from .models import About
from hitcount.views import HitCountDetailView


class AboutListView(ListView):
   model = About
   template_name = 'about.html'
   context_object_name = 'abouts'

class AboutDetailView(HitCountDetailView):
    model = About
    template_name = 'team_details.html'
    context_object_name = 'about'
    slug_field = 'slug'
    # set to True to count the hit
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(AboutDetailView, self).get_context_data(**kwargs)
        context.update({
        'popular_teams': About.objects.order_by('-hit_count_generic__hits')[:3],
        })
        return context

