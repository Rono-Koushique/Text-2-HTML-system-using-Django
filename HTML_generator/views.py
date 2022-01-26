from django.shortcuts import render
from .models import Content
from .forms import ContentForm


# Create your views here.
def home(request):
    context = {
        'title' : 'Text-HTML generator',
        'form' : ContentForm(),
    }
    
    return render(request, "HTML_generator/home.html", context)