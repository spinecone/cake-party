from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.

class RootView(TemplateView):
    template_name = "root.html"

