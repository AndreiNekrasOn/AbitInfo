from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import *


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
    olymps = list(Olymp.objects.order_by('title'))
    if 'olymp_name' in request.GET and request.GET['olymp_name']:
        olymp_name = request.GET['olymp_name']
        univers = Univer_plus.objects.order_by('rating', 'title').filter(olymps__title=olymp_name)
        set_univers = set()
        for u in univers:
            set_univers.add(u)
        content = {'olymp_name': olymp_name, 'subjects': subjects, 'univers': set_univers, 'olymps': olymps}
        return render_to_response('olcalc/index.html', content)
    else:
        return render(request, 'olcalc/index.html', {'subjects': subjects, 'olymps': olymps})
