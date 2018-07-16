from django.shortcuts import render

# Create your views here.

from .models import Olymp, Speciality, Faculty, University, Subject

def index(request):
    return render(request, 'olcalc/index.html', {})