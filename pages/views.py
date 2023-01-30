from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

def homepage(request):
    return HttpResponse("Hello World!")

class mainpage(TemplateView):
    template_name = "index.html"
    