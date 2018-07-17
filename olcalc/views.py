from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import Olymp, Speciality, Faculty, University, Subject

def index(request):
    subjects = Subject.objects.order_by('title')
    olymps = Olymp.objects.order_by('title')
    return render(request, 'olcalc/index.html', {'subjects': subjects, 'olymps': olymps})

def test(request):
    subjects = Subject.objects.order_by('title')
    olymps = Olymp.objects.order_by('title')
    return render(request, 'olcalc/test.html', {'subjects': subjects, 'olymps': olymps})

def search(request):
    subjects = Subject.objects.order_by('title')
    olymps = Olymp.objects.order_by('title')
    if 'olymp_name' in request.GET and request.GET['olymp_name']:
        olymp_name = request.GET['olymp_name']
        univers = University.objects.order_by('title')
        specialities=Speciality.objects.order_by('title')
        faculties = Faculty.objects.order_by('title')
        #univols = University.faculties.all
        return render_to_response('olcalc/test.html', {
            'olymp_name': olymp_name, 'subjects': subjects, 'olymps': olymps, 
            'univers': univers, 'specialities': specialities, 'faculties': faculties, 
            #'univols': univols
        })
    else:
        return render(request, 'olcalc/test.html', {'subjects': subjects, 'olymps': olymps})