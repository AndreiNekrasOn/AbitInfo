from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import Olymp, Univer_plus, Subject

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
        univers=Univer_plus.objects.order_by('rating', 'title').filter(olymps__title=olymp_name)
        qUnivers=[]
        
        
        content = {'olymp_name': olymp_name, 'subjects': subjects, 'univers': univers, 'olymps': olymps}
        
        return render_to_response('olcalc/test.html', content)
    else:
        return render(request, 'olcalc/test.html', {'subjects': subjects, 'olymps': olymps})