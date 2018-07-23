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
    olymps = Olymp.objects.order_by('rating')
    return render(request, 'olcalc/test.html', {'subjects': subjects, 'olymps': olymps})

def search(request):
    subjects = Subject.objects.order_by('title')
    olymps = Olymp.objects.order_by('title')
    if 'olymp_name' in request.GET and request.GET['olymp_name']:
        olymp_name = request.GET['olymp_name']
        qUnivers = Univer_plus.objects.order_by('title')
        univer=[]
        oRange = []
        num_of_univers=[]
        i = 0
        for u in qUnivers:
            univer.append(u)
            num_of_univers.append(i)
            i+=1
        k = univer[0].olymps.all().query
        
        return render_to_response('olcalc/test.html', {'olymp_name': olymp_name, 'subjects': subjects, 'olymps': olymps,
                    'univer': univer, 'num_of_univers': num_of_univers ,
                    'k': k
          })
    else:
        return render(request, 'olcalc/test.html', {'subjects': subjects, 'olymps': olymps})